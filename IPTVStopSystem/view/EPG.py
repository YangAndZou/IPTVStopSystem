# coding=utf-8
import base64

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from utils import utils
from IPTVStopSystem.models import IPTVAuthCode, IPTVProgramOperationLog
from IPTVStopSystem.models import IPTVEPG


@login_required()
def show_epg(request):
    epg = IPTVEPG.objects.all()
    while True:
        auth_codes = IPTVAuthCode.objects.all()
        if len(auth_codes) == 0:
            code = base64.encodestring('q1234567')
            IPTVAuthCode.objects.create(auth_code=code)
        else:
            break
    # 初始化epg状态为2（开启）
    if len(epg) == 0:
        IPTVEPG.objects.create(status=2)
    status = IPTVEPG.objects.all()[0].status
    return render(request, 'epg/epg.html', {'status': status})


@login_required()
def epg_one_key(request):
    if request.method == 'POST':
        # 取到前端传入的授权码
        auth_code = request.POST.get('code')
        # 取出数据库中的授权码(只有一个)
        auth_code_from_db = base64.decodestring(IPTVAuthCode.objects.get(id=1).auth_code)
        if auth_code == auth_code_from_db:
            mode = request.POST.get('mode')
            ip = '192.168.2.168'
            port = '22'
            username = 'root'
            passwd = 'Trans@2017'
            cmd = ''
            if mode == 'turn_off':
                mode = '关停'
                real_cmd = utils.epg_shutdown_cmd()
                cmd = utils.test_create_code('epg关停', '关停epg')
                utils.ssh_paramiko(ip, port, username, passwd, cmd)
                IPTVEPG.objects.filter(id=1).update(status=1)
            elif mode == 'turn_on':
                mode = '开启'
                cmd = utils.test_create_code('epg开启', '开启epg')
                utils.ssh_paramiko(ip, port, username, passwd, cmd)
                IPTVEPG.objects.filter(id=1).update(status=2)

                # 插入日志

            # 插入日志，直接插在频道日志里了
            IPTVProgramOperationLog.objects.create(program_id=1,
                                                   content='用户 {} 执行 EPG 一键 {} 操作，操作命令：'.
                                                   format(request.user.username, mode, cmd))
            return JsonResponse({'code': '200', 'msg': '操作成功！'})
        else:
            return JsonResponse({'code': '201', 'msg': '请输入正确的授权码！'})
