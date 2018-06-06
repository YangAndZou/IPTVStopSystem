# coding=utf-8
import base64
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from IPTVStopSystem import utils
from IPTVStopSystem.models import IPTVProgram
from IPTVStopSystem.models import IPTVAuthCode


def show_process_verify(request):
    if request.user.is_superuser:
        return HttpResponse('您没有查看授权码的权限!')
    else:
        auth_codes = IPTVAuthCode.objects.all()
        if len(auth_codes) > 0:
            code = base64.decodestring(auth_codes[0].auth_code)
        else:
            code = base64.encodestring('123456789')
            IPTVAuthCode.objects.create(auth_code=code)
        return render(request, 'process_verify/process_verify.html', {'code': code})


def set_auth_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        secret_code = base64.encodestring(code)
        IPTVAuthCode.objects.filter(id=1).update(auth_code=secret_code)
        return JsonResponse({'msg': 'ok'})
#
# def process_verify(request):
#     if request.method == 'POST':
#         mode = request.POST.get('mode')
#         process_id = request.POST.get('process_id')
#         process = IPTVProcessVerify.objects.filter(id=process_id)
#         process_type = process[0].get_process_type_display()
#         operation_type = process[0].get_operation_type_display()
#         operation_target = process[0].operation_target
#         programs = IPTVProgram.objects.all()
#         # 是否通过审核
#         if mode == 'pass':
#             process.update(status=3)
#             if operation_type == 'turn_off':
#                 # TODO 1 EPG
#                 if process_type == 'EPG关停':
#                     pass
#                 # 2 直播
#                 elif process_type == '直播频道关停':
#                     if operation_type == '关停':
#                         utils.ssh_paramiko('192.168.2.168', 'root', 'Trans@2017',
#                                            'rm -rf /home/transfar/oooooooooooooooooooooops')
#                         if operation_target == [u'all']:
#                             programs.update(status=1)
#                         programs.filter(program_name__in=operation_target).update(status=1)
#                     elif operation_type == '恢复':
#                         utils.ssh_paramiko('192.168.2.168', 'root', 'Trans@2017',
#                                            'touch /home/transfar/oooooooooooooooooooooops')
#                         if operation_target == [u'all']:
#                             programs.update(status=2)
#                         programs.filter(program_name__in=operation_target).update(status=2)
#                 # TODO 3 CDN
#                 elif process_type == 'CDN关停':
#                     pass
#             elif operation_type == 'turn_on':
#                 if process_type == 1:
#                     pass
#                 # 2 直播
#                 elif process_type == 2:
#                     pass
#                 # TODO 3 CDN
#                 elif process_type == 3:
#                     pass
#         # TODO 审核不通过的回退操作
#         elif mode == 'reject':
#             suggestion = request.POST.get('suggestion')
#             if suggestion:
#                 process.update(suggestion=suggestion)
#             process.update(status=2)
