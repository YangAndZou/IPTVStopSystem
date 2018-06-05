# coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from IPTVStopSystem import utils
from IPTVStopSystem.models import IPTVCDNNode
from IPTVStopSystem.models import IPTVCDNOperationLog


def show_cdn(request, platform, city, pop_node):
    nodes = IPTVCDNNode.objects.all()
    print(platform)
    print(city)
    print(pop_node)
    if platform != '0':
        nodes.filter(platform=platform)
    if city != '0':
        nodes.filter(city__contains=city)
    if pop_node != '0':
        nodes.filter(node_name__contains=pop_node)
    return render(request, 'cdn/cdn.html', {'nodes': nodes})


# 显示操作记录
def show_log(request):
    logs = IPTVCDNOperationLog.objects.all()
    return render(request, 'cdn/cdn_logs.html', {'cdn_logs': logs})


def cdn_change(request):
    return HttpResponse('hello')
