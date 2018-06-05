# coding=utf-8
import json

from django.http import JsonResponse
from django.shortcuts import render
from IPTVStopSystem.models import IPTVProgramOperationLog
from IPTVStopSystem.models import IPTVProgram
from IPTVStopSystem.models import IPTVProcessVerify


def show_program(request, program_name, program_ip, program_num, status):
    if request.method == 'GET':
        programs = IPTVProgram.objects.all()
        # 以下为搜索功能，分别对应频道名，频道ip，状态
        if program_name != '0':
            programs = programs.filter(program_name__contains=program_name)
        if program_ip != '0':
            programs = programs.filter(program_ip__contains=program_ip)
        # TODO 等待前端完成program_num的传值
        # if program_num != '0':
        #     start = program_num.split('-')[0]
        #     end = program_num.split('-')[1]
        #     programs = programs.filter(program_num__range=(start, end))
        if status != '0':
            programs = programs.filter(status=status)
        return render(request, 'program/program.html', {'programs': programs})


# 关停 / 开启
def program_change(request):
    if request.method == 'POST':
        try:
            mode = request.POST.get('mode')
            # program_ips 接收的数据有两种格式： 当全选时，接收的数据为 ['all']，
            # 当部分选中时，接收的数据为['192.168...', '192.168...', ...]
            # TODO 改成传频道名称
            program_names = json.loads(request.POST.get('program_names'))
            print(program_names)
            print(mode)
            if mode == 'turn_off':
                # 1 为关停
                mode = 1
            elif mode == 'turn_on':
                # 2 为恢复
                mode = 2
            # 向管理员发起请求，但是不会重复发送
            pv = IPTVProcessVerify.objects.filter(operation_target=program_names, status=1)
            print(mode)
            if len(pv) > 0:
                return JsonResponse({'error': '您提交的请求正在审核中，请耐心等待', 'code': '201'})
            else:
                IPTVProcessVerify.objects.create(
                    process_type=2,
                    operation_target=program_names,
                    status=1,
                    operation_type=mode
                )
                return JsonResponse({'success': '已提交请求！', 'code': '200'})
        except Exception as e:
            print(e)
            return JsonResponse({'msg': e, 'code': "201"})


# 显示操作记录
def show_log(request):
    logs = IPTVProgramOperationLog.objects.all()
    return render(request, 'program/program_logs.html', {'program_logs': logs})
