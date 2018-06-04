# coding=utf-8
import json

from django.http import JsonResponse
from django.shortcuts import render
from IPTVStopSystem import utils
from IPTVStopSystem.models import IPTVProgramOperationLog
from IPTVStopSystem.models import IPTVProgram


def show_program(request, program_name, program_ip, program_num, status):
    if request.method == 'GET':
        programs = IPTVProgram.objects.all()
        # 以下为搜索功能，分别对应频道名，频道ip，状态
        if program_name != '0':
            programs = programs.filter(program_name__contains=program_name)
        if program_ip != '0':
            programs = programs.filter(program_ip__contains=program_ip)
        if program_num != '0':
            start = program_num.split('-')[0]
            end = program_num.split('-')[1]
            programs = programs.filter(program_num__range=(start, end))
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
            program_ips = json.loads(request.POST.get('program_ips'))
            programs = IPTVProgram.objects.all()
            if mode == 'turn_off':
                utils.ssh_paramiko('192.168.2.168', 'root', 'Trans@2017',
                                   'rm -rf /home/transfar/oooooooooooooooooooooops')
                if program_ips == [u'all']:
                    programs.update(status=1)
                programs.filter(program_ip__in=program_ips).update(status=1)
            elif mode == 'turn_on':
                utils.ssh_paramiko('192.168.2.168', 'root', 'Trans@2017',
                                   'touch /home/transfar/oooooooooooooooooooooops')
                if program_ips == [u'all']:
                    programs.update(status=2)
                programs.filter(program_ip__in=program_ips).update(status=2)
            return JsonResponse({'msg': 'ok', 'code': "200"})
        except Exception as e:
            print(e)
            return JsonResponse({'msg': e, 'code': "201"})


# 显示操作记录
def show_log(request):
    logs = IPTVProgramOperationLog.objects.all()
    return render(request, 'program/program_logs.html', {'program_logs': logs})
