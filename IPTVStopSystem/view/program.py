# coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render
from IPTVStopSystem import utils
from IPTVStopSystem.models import IPTVProgramOperationLog
from IPTVStopSystem.models import IPTVProgram


# 关停 / 开启
def program_change(request):
    if request.method == 'POST':
        try:
            mode = request.POST.get('mode')
            program_ips = request.POST.get('program_ips')
            programs = IPTVProgram.objects.all()
            if mode == 'turn_off':
                # for ip in program_ips:
                #     utils.ssh_paramiko(ip, 'root', '12', 'turn off')
                programs.filter(program_ip__in=program_ips).update(status=1)
            elif mode == 'turn_on':
                # for ip in program_ips:
                #     utils.ssh_paramiko(ip, 'root', '12', 'turn on')
                programs.filter(program_ip__in=program_ips).update(status=2)
            return JsonResponse({'msg': 'ok', 'code': "200"})
        except Exception as e:
            print(e)
            return JsonResponse({'msg': e, 'code': "201"})


# 显示操作记录
def show_log(request):
    logs = IPTVProgramOperationLog.objects.all()
    return render(request, 'program_logs.html', {'program_logs': logs})