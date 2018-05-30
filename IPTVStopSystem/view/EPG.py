# coding=utf-8
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from IPTVStopSystem import utils
from IPTVStopSystem.models import IPTVSystem
from IPTVStopSystem.models import IPTVEPGOperationLog


def epg(request, system_attr, system_val, router_group):
    systems = IPTVSystem.objects.all()
    if system_attr != '0':
        print(system_attr)
    if system_val != '0':
        print(system_val)
    if router_group != '0':
        systems.filter(router_group__router_name__contains=router_group)
    return render(request, 'epg/epg.html', {"systems": systems})


# 显示操作记录
def show_log(request):
    logs = IPTVEPGOperationLog.objects.all()
    return render(request, 'epg/epg_logs.html', {'html': logs})


def epg_change(request):
    return HttpResponse('hello')
