# coding=utf-8
import base64

import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from IPTVStopSystem import utils
from IPTVStopSystem.models import IPTVCDNNode, IPTVAuthCode
from IPTVStopSystem.models import IPTVCDNOperationLog


@login_required()
def show_cdn(request, platform, city, pop_node):
    nodes = IPTVCDNNode.objects.all()
    if platform != '0':
        nodes.filter(platform=platform)
    if city != '0':
        nodes.filter(city__contains=city)
    if pop_node != '0':
        nodes.filter(node_name__contains=pop_node)
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
        if auth_code == auth_code_from_db:
            ip = '192.168.2.168'
            port = '22'
            username = 'root'
            passwd = 'Trans@2017'
            # real_cmd = utils.huawei_cdn_shutdown_cmd()
            # real_cmd2 = utils.ZTE_cdn_pop_shutdown_cmd(90)
            # real_cmd3 = utils.ZTE_cdn_shutdown_cmd()
            test_cmd = utils.test_create_code('cdn关停', '关停cdn')
            mode = request.POST.get('mode')
            node_ids = request.POST.get('node_ids')

            node_ids = node_ids[1:-1]
            node_list = node_ids.split(',')

            # 1 为关停 2 为恢复
            if mode == 'turn_off':
                mode = '关停'
            elif mode == 'turn_on':
                mode = '恢复'

            for node_id in node_list:
                node_id = int(node_id)
                node_name = IPTVCDNNode.objects.get(id=node_id).node_name
                if mode == '关停':
                    IPTVCDNNode.objects.filter(id=node_id).update(status=1)
                    utils.ssh_paramiko(ip, port, username, passwd, test_cmd)
                elif mode == '恢复':
                    IPTVCDNNode.objects.filter(id=node_id).update(status=2)
                    utils.ssh_paramiko(ip, port, username, passwd, test_cmd)

                # 插入日志
                IPTVCDNOperationLog.objects.create(cdn_id=node_id,
                                                   content='用户 {} 对 {} 节点执行 {} 操作，执行命令 {}'.
                                                   format(request.user.username, node_name, mode, test_cmd))

            return JsonResponse({'code': '200', 'msg': 'CDN关停成功！'})
        else:
            return JsonResponse({'code': '201', 'msg': '请输入正确的授权码！'})
