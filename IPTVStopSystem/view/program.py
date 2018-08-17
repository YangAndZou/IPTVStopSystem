# coding=utf-8
import base64
import json

import time
import datetime

from utils import utils, optimizations
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from IPTVStopSystem.models import IPTVLiveProgramLog
from IPTVStopSystem.models import IPTVLiveProgram
# from IPTVStopSystem.models import IPTVAuthCode
from IPTVStopSystem import settings


@login_required()
def show_program(request, program_name, program_type, platform, status, program_ip_type):
    if request.method == 'GET':
        programs = IPTVLiveProgram.objects.all().order_by('id')
        # 以下为搜索功能，分别对应频道名，频道类型（收费，省内...），平台（中兴，华为...），状态，ip类型（iptv, iptv+）他们的值默认为0
        if program_name != '0':
            programs = programs.filter(program_name__contains=program_name)
        if program_type != '0':
            programs = programs.filter(program_type=program_type)
        if platform != '0':
            programs = programs.filter(platform=platform)
        if status != '0':
            programs = programs.filter(status=status)
        if program_ip_type != '0':
            programs = programs.filter(program_ip_type=program_ip_type)

        program_ids = [program.id for program in programs]
        return render(request, 'program/program.html', {'programs': programs, 'program_ids': program_ids})


@login_required()
def show_log(request, start_time, end_time):
    logs = IPTVLiveProgramLog.objects.all().order_by('-id')
    if len(start_time) > 7 and len(end_time) > 7:
        # 由于得到的datetime没有带时间，所以时间为00:00:00，即2018-06-07 00:00:00，
        # 所以需要将天数加 1 天
        real_end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')
        real_end_time += datetime.timedelta(days=1)
        real_end_time = real_end_time.strftime('%Y-%m-%d')
        logs = logs.filter(update_time__range=(start_time, real_end_time))

    return render(request, 'program/program_logs.html', {'program_logs': logs})


# 搜索时的模糊匹配
@login_required()
def approximate(request):
    if request.method == 'POST':
        name = request.POST.get('program_name')
        search_names = IPTVLiveProgram.objects.filter(program_name__contains=name)
        names = []
        for name in search_names:
            names.append(name.program_name)
        if len(search_names) > 0:
            return JsonResponse({'search_names': names})
        else:
            return JsonResponse({'search_names': 'undefined'})


@login_required()
# def program_change(request):
#     if request.method == 'POST':
#         start = time.time()
#         # 取到前端传入的授权码
#         auth_code = request.POST.get('code')
#         # 取出数据库中的授权码(只有一个)
#         auth_code_from_db = base64.decodestring(IPTVAuthCode.objects.first().auth_code)
#         if auth_code == auth_code_from_db:
#             ip = settings.IPTV_IP
#             port = settings.IPTV_PORT
#             username = settings.IPTV_USERNAME
#             passwd = settings.IPTV_PASSWD
#
#             mode = request.POST.get('mode')
#             # program_ids 为json格式的字符串，格式为 '['1','2',]', 所以需要做字符串处理
#             program_ids = request.POST.get('program_ids')
#             program_list = json.loads(program_ids)
#             # program_ids = program_ids[1:-1]
#             # program_list = program_ids.split(',')
#
#             # 将Mode改成中文,便于日志记录
#             if mode == 'turn_off':
#                 mode = '关停'
#             elif mode == 'turn_on':
#                 mode = '恢复'
#
#             # 命令列表, 传入多线程队列中
#             cmds = []
#             cmd = ''
#             # 创建封装的多线程对象
#             work_manager = optimizations.WorkManager(ip, port, username, passwd, 4)
#             for program_id in program_list:
#                 program_id = int(program_id)
#                 program_name = IPTVProgram.objects.get(id=program_id).program_name
#                 program_ip = IPTVProgram.objects.get(id=program_id).program_ip
#
#                 if mode == '关停':
#                     # 更新频道状态
#                     IPTVProgram.objects.filter(id=program_id).update(status=1)
#                     cmd = utils.test_create_code(program_ip)
#                 elif mode == '恢复':
#                     IPTVProgram.objects.filter(id=program_id).update(status=2)
#                     cmd = utils.test_rm_code(program_ip)
#                 cmds.append(cmd)
#                 # 插入日志
#                 IPTVProgramOperationLog.objects.create(program_id=program_id,
#                                                        content='用户 {} 对 {} 频道执行 {} 操作，执行命令 {}'.
#                                                        format(request.user.username, program_name, mode, cmd))
#             # 以 10 为倍数计算命令总数
#             count = len(cmds) / 10 if len(cmds) % 10 == 0 else (len(cmds) / 10) + 1
#             for i in range(count):
#                 run_cmds = cmds[10 * i: (i + 1) * 10]
#                 run_cmd = ';'.join(run_cmds)
#                 # 将处理后的命令加入队列中
#                 work_manager.add_job(ssh_paramiko(work_manager.ssh, run_cmd))
#             # 多线程处理队列
#             work_manager.wait_allcomplete()
#             end = time.time()
#             print('run time--------->', end - start)
#             return JsonResponse({'success': '操作成功！', 'msg': 'ok', 'code': '200'})
#         else:
#             return JsonResponse({'error': '请输入正确的授权码！', 'msg': 'error', 'code': '201'})


# paramiko ssh 操作封装

def ssh_paramiko(ssh, cmd):
    try:
        # 当执行多条命令时，需要让get_pty=True，执行多条命令的格式为"cd /home;ls;cat z"
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
    except Exception as e:
        print('%s Error,\n' % e)
