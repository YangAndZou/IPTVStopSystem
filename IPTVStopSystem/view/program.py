# coding=utf-8
import base64
import time

from IPTVStopSystem import utils
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from IPTVStopSystem.models import IPTVProgramOperationLog
from IPTVStopSystem.models import IPTVProgram
from IPTVStopSystem.models import IPTVAuthCode
from IPTVStopSystem import optimizations


@login_required()
def show_program(request, program_name, program_type, platform, status, program_ip_type):
    if request.method == 'GET':
        programs = IPTVProgram.objects.all()
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


# 关停 / 开启
@login_required()
def program_change(request):
    if request.method == 'POST':
        start = datetime.datetime.now()
        # 取到前端传入的授权码
        auth_code = request.POST.get('code')
        # 取出数据库中的授权码(只有一个)
        auth_code_from_db = base64.decodestring(IPTVAuthCode.objects.get(id=1).auth_code)
        if auth_code == auth_code_from_db:
            ip = '192.168.2.168'
            port = '22'
            username = 'root'
            passwd = 'Trans@2017'
            mode = request.POST.get('mode')
            # program_ids 为字符串，格式为 '['1','2',]'
            program_ids = request.POST.get('program_ids')
            program_ids = program_ids[1:-1]
            program_list = program_ids.split(',')
            # 1 为关停 2 为恢复
            if mode == 'turn_off':
                mode = '关停'
            elif mode == 'turn_on':
                mode = '恢复'

            ssh = utils.SSH2(ip, port, username, passwd)
            ssh.run(range(1, 200))

            print('运行中时间---------====》', datetime.datetime.now())

            ips = []
            for program_id in program_list:
                program_id = int(program_id)
                program_name = IPTVProgram.objects.get(id=program_id).program_name
                program_ip = IPTVProgram.objects.get(id=program_id).program_ip
                ips.append(program_ip)
                cmd = ''
                if mode == '关停':
                    IPTVProgram.objects.filter(id=program_id).update(status=1)
                elif mode == '恢复':
                    IPTVProgram.objects.filter(id=program_id).update(status=2)
                # 插入日志
                IPTVProgramOperationLog.objects.create(program_id=program_id,
                                                       content='用户 {} 对 {} 频道执行 {} 操作，执行命令 {}'.
                                                       format(request.user.username, program_name, mode, cmd))

            ssh.close_ssh()
            end = datetime.datetime.now()
            print('运行时间---------====》', end - start)

            return JsonResponse({'success': '操作成功！', 'msg': 'ok'})
        else:
            return JsonResponse({'error': '请输入正确的授权码！', 'msg': 'error'})


def shutdown(queue, ip, port, username, passwd):
    while True:
        program_ip = queue.get()
        cmd = utils.test_create_code(program_ip, 'YoYo')
        utils.ssh_paramiko(ip, port, username, passwd, cmd)
        queue.task_done()


@login_required()
def show_log(request, start_time, end_time):
    logs = IPTVProgramOperationLog.objects.all().order_by('-id')
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
        search_names = IPTVProgram.objects.filter(program_name__contains=name)
        names = []
        for name in search_names:
            names.append(name.program_name)
        if len(search_names) > 0:
            return JsonResponse({'search_names': names})
        else:
            return JsonResponse({'search_names': 'undefined'})


@login_required()
def program_change(request):
    if request.method == 'POST':
        f1_start = time.time()
        # 取到前端传入的授权码
        auth_code = request.POST.get('code')
        # 取出数据库中的授权码(只有一个)
        auth_code_from_db = base64.decodestring(IPTVAuthCode.objects.get(id=1).auth_code)
        if auth_code == auth_code_from_db:
            ip = '192.168.2.168'
            port = 22
            username = 'root'
            passwd = 'Trans@2017'

            mode = request.POST.get('mode')
            # program_ids 为字符串，格式为 '['1','2',]'
            program_ids = request.POST.get('program_ids')
            program_ids = program_ids[1:-1]
            program_list = program_ids.split(',')

            # 1 为关停 2 为恢复
            if mode == 'turn_off':
                mode = '关停'
            elif mode == 'turn_on':
                mode = '恢复'

            ips = []
            for program_id in program_list:
                program_id = int(program_id)
                program_name = IPTVProgram.objects.get(id=program_id).program_name
                program_ip = IPTVProgram.objects.get(id=program_id).program_ip
                ips.append(program_ip)
                cmd = ''
                if mode == '关停':
                    IPTVProgram.objects.filter(id=program_id).update(status=1)
                    cmd = utils.test_create_code(program_ip, program_ip)
                elif mode == '恢复':
                    IPTVProgram.objects.filter(id=program_id).update(status=2)
                    cmd = utils.test_rm_code(program_ip, program_ip)
                # 插入日志
                # IPTVProgramOperationLog.objects.create(program_id=program_id,
                #                                        content='用户 {} 对 {} 频道执行 {} 操作，执行命令 {}'.
                #                                        format(request.user.username, program_name, mode, cmd))
            f1_end = time.time()
            print('load time--------->', f1_end - f1_start)
            print(ips)
            start = time.time()
            work_manager = optimizations.WorkManager(ip, port, username, passwd, ips, 100)
            work_manager.wait_allcomplete()
            end = time.time()
            print('run time--------->', end - start)
            return JsonResponse({'success': '操作成功！', 'msg': 'ok'})
        else:
            return JsonResponse({'error': '请输入正确的授权码！', 'msg': 'error'})
