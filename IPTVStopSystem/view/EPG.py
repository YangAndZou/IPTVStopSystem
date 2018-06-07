# coding=utf-8
import base64

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from IPTVStopSystem import utils
from IPTVStopSystem.models import IPTVAuthCode


@login_required()
def show_epg(request):
    return render(request, 'epg/epg.html')


@login_required()
def epg_one_key(request):
    if request.method == 'POST':
        # 取到前端传入的授权码
        auth_code = request.POST.get('code')
        # 取出数据库中的授权码(只有一个)
        auth_code_from_db = base64.decodestring(IPTVAuthCode.objects.get(id=1).auth_code)
        if auth_code == auth_code_from_db:
            real_cmd = utils.epg_shutdown_cmd()
            test_cmd = utils.test_create_code('epg关停', '关停epg')
            ip = '192.168.2.168'
            port = '22'
            username = 'root'
            passwd = 'Trans@2017'
            utils.ssh_paramiko(ip, port, username, passwd, test_cmd)
            return JsonResponse({'code': '200', 'msg': 'EPG关停成功！'})
        else:
            return JsonResponse({'code': '201', 'msg': '请输入正确的授权码！'})
