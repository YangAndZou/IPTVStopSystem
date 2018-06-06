# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from IPTVStopSystem import utils
from IPTVStopSystem.models import IPTVProcessVerify
from IPTVStopSystem.models import IPTVProgram


def show_process_verify(request):
    if request.user.is_superuser:
        # 仅显示需要审核的流程
        verifies = IPTVProcessVerify.objects.filter(status=1)
        return render(request, 'process_verify/process_verify.html', {'verifies': verifies})
    else:
        return HttpResponse('搞咩呀!')

def process_verify(request):
    if request.method == 'POST':
        mode = request.POST.get('mode')
        process_id = request.POST.get('process_id')
        process = IPTVProcessVerify.objects.filter(id=process_id)
        process_type = process[0].get_process_type_display()
        operation_type = process[0].get_operation_type_display()
        operation_target = process[0].operation_target
        programs = IPTVProgram.objects.all()
        # 是否通过审核
        if mode == 'pass':
            process.update(status=3)
            if operation_type == 'turn_off':
                # TODO 1 EPG
                if process_type == 'EPG关停':
                    pass
                # 2 直播
                elif process_type == '直播频道关停':
                    if operation_type == '关停':
                        utils.ssh_paramiko('192.168.2.168', 'root', 'Trans@2017',
                                           'rm -rf /home/transfar/oooooooooooooooooooooops')
                        if operation_target == [u'all']:
                            programs.update(status=1)
                        programs.filter(program_name__in=operation_target).update(status=1)
                    elif operation_type == '恢复':
                        utils.ssh_paramiko('192.168.2.168', 'root', 'Trans@2017',
                                           'touch /home/transfar/oooooooooooooooooooooops')
                        if operation_target == [u'all']:
                            programs.update(status=2)
                        programs.filter(program_name__in=operation_target).update(status=2)
                # TODO 3 CDN
                elif process_type == 'CDN关停':
                    pass
            elif operation_type == 'turn_on':
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
