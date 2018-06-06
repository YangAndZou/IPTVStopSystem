# coding=utf-8
import base64
import json

from django.http import JsonResponse
from django.shortcuts import render
from IPTVStopSystem.models import IPTVProgramOperationLog
from IPTVStopSystem.models import IPTVProgram
from IPTVStopSystem.models import IPTVAuthCode


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
        return render(request, 'program/program.html', {'programs': programs})


# 关停 / 开启
def program_change(request):
    if request.method == 'POST':
        # 取到前端传入的授权码
        auth_code = request.POST.get('code')
        # 取出数据库中的授权码(只有一个)
        auth_code_from_db = base64.decodestring(IPTVAuthCode.objects.get(id=1))

        if auth_code == auth_code_from_db:
            mode = request.POST.get('mode')
            # program_ids 为列表
            program_ids = request.POST.get('program_id')

            # 1 为关停 2 为恢复
            if mode == 'turn_off':
                mode = '关停'
            elif mode == 'turn_on':
                mode = '恢复'

            # 插入日志
            for program_id in program_ids:
                program_name = IPTVProgram.objects.get(id=program_id).program_name
                IPTVProgramOperationLog.objects.create(program_id=program_id,
                                                       content='用户 {} 对 {} 频道执行 {} 操作'.
                                                       format(request.user.username, program_name, mode))
            return JsonResponse({'success': '操作成功！'})
        else:
            return JsonResponse({'error': '请输入正确的授权码！'})


def program_turn_off(request):
    return JsonResponse({'success': '关停成功'})


def program_turn_on(request):
    return JsonResponse({'success', '恢复成功'})


def show_log(request):
    logs = IPTVProgramOperationLog.objects.all()
    return render(request, 'program/program_logs.html', {'program_logs': logs})


# 搜索时的模糊匹配
def approximate(request):
    if request.method == 'POST':
        name = request.POST.get('program_name')
        print(name)
        search_names = IPTVProgram.objects.filter(program_name__contains=name)
        print(search_names)
        print(json.loads(search_names))
        return JsonResponse({'search_names': 'a'})
