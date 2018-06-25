# coding=utf-8
import base64

import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from IPTVStopSystem import utils, settings, optimizations
from IPTVStopSystem.models import IPTVCDNNode, IPTVAuthCode
from IPTVStopSystem.models import IPTVCDNOperationLog


@login_required()
def show_cdn(request, platform, city):
    nodes = IPTVCDNNode.objects.all()
    if platform != '0':
        nodes = nodes.filter(paltform=platform)
    if city != '0':
        cities = city.split(',')
        nodes = nodes.filter(city__in=cities)
    node_ids = [node.id for node in nodes]
    return render(request, 'cdn/cdn.html', {'nodes': nodes, 'node_ids': node_ids})


# 显示操作记录
@login_required()
def show_log(request, start_time, end_time):
    logs = IPTVCDNOperationLog.objects.all().order_by('-id')
    if len(start_time) > 7 and len(end_time) > 7:
        # 由于得到的datetime没有带时间，所以时间为00:00:00，即2018-06-07 00:00:00，
        # 所以需要将天数加 1 天
        real_end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')
        real_end_time += datetime.timedelta(days=1)
        real_end_time = real_end_time.strftime('%Y-%m-%d')
        logs = logs.filter(update_time__range=(start_time, real_end_time))
    return render(request, 'cdn/cdn_logs.html', {'cdn_logs': logs})


@login_required()
def cdn_change(request):
    if request.method == 'POST':
        # 取到前端传入的授权码
        auth_code = request.POST.get('code')
        # 取出数据库中的授权码(只有一个)
        auth_code_from_db = base64.decodestring(IPTVAuthCode.objects.get(id=1).auth_code)
        print('---------------')
        print(auth_code)
        print(auth_code_from_db)
        if auth_code == auth_code_from_db:
            ip = settings.IPTV_IP
            port = settings.IPTV_PORT
            username = settings.IPTV_USERNAME
            passwd = settings.IPTV_PASSWD

            mode = request.POST.get('mode')
            node_ids = request.POST.get('node_ids')
            print('------------ ')
            print(node_ids)
            node_list = json.loads(node_ids)

            # 1 为关停 2 为恢复
            if mode == 'turn_off':
                mode = '关停'
            elif mode == 'turn_on':
                mode = '恢复'

            # 命令列表, 传入多线程队列中
            cmds = []
            cmd = ''
            # 创建封装的多线程对象
            work_manager = optimizations.WorkManager(ip, port, username, passwd, 4)

            for node_id in node_list:
                node_id = int(node_id)
                node_name = IPTVCDNNode.objects.get(id=node_id).device_name
                node_ip = IPTVCDNNode.objects.get(id=node_id).ip

                if mode == '关停':
                    IPTVCDNNode.objects.filter(id=node_id).update(status=1)
                    cmd = utils.test_create_code(node_ip)
                elif mode == '恢复':
                    IPTVCDNNode.objects.filter(id=node_id).update(status=2)
                    cmd = utils.test_create_code(node_ip)
                cmds.append(cmd)
                # 插入日志
                IPTVCDNOperationLog.objects.create(cdn_id=node_id,
                                                   content='用户 {} 对 {} 节点执行 {} 操作，执行命令 {}'.
                                                   format(request.user.username, node_name, mode, cmd))

                # 以 10 为倍数计算命令总数
            count = len(cmds) / 10 if len(cmds) % 10 == 0 else (len(cmds) / 10) + 1
            for i in range(count):
                run_cmds = cmds[10 * i: (i + 1) * 10]
                run_cmd = ';'.join(run_cmds)
                # 将处理后的命令加入队列中
                work_manager.add_job(ssh_paramiko(work_manager.ssh, run_cmd))
                # 多线程处理队列
            work_manager.wait_allcomplete()
            return JsonResponse({'success': '操作成功！', 'msg': 'ok', 'code': '200'})
        else:
            return JsonResponse({'code': '201', 'msg': '请输入正确的授权码！'})


# paramiko ssh 操作封装
def ssh_paramiko(ssh, cmd):
    try:
        # 当执行多条命令时，需要让get_pty=True，执行多条命令的格式为"cd /home;ls;cat z"
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
    except Exception as e:
        print('%s Error,\n' % e)