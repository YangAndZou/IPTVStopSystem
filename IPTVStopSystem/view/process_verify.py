# coding=utf-8
from django.shortcuts import render

from IPTVStopSystem.models import IPTVProcessVerify


def show_process_verify(request):
    # 仅显示需要审核的流程
    verifies = IPTVProcessVerify.objects.filter(status=1)
    return render(request, 'auditingFlow/auditingFlow.html', {'verifies': verifies})


def process_verify(request):
    if request.method == 'POST':
        mode = request.POST.get('mode')
        process_id = request.POST.get('process_id')
        process = IPTVProcessVerify.objects.filter(id=process_id)
        process_type = process[0].operation_type
        operation_type = process[0].operation
        # 是否通过审核
        if mode == 'pass':
            process.update(status=3)
            # TODO 1 EPG
            if process_type == 1:
                pass
            # 2 直播
            elif process_type == 2:
                pass
            # TODO 3 CDN
            elif process_type == 3:
                pass
        # TODO 审核不通过的回退操作
        elif mode == 'reject':
            suggestion = request.POST.get('suggestion')
            if suggestion:
                process.update(suggestion=suggestion)
            process.update(status=2)
