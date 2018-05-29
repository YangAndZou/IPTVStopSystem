# coding=utf-8
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from models import IPTVProgram
from models import IPTVProgramOperationLog
import utils


# 登录验证
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        print('session', request.session.get('username'))
        if request.session.get('username') is not None:
            return HttpResponseRedirect('/', {"user": request.user})
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print('username', username)
            print('password', password)
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                request.session['username'] = username
                return HttpResponseRedirect('/', {"user": request.user})
            return render(request, 'login.html', {"login_error_info": "用户名或者密码错误！"})


# 登录
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')


# 用户没有权限时触发
def noperm(request):
    return render(request, 'noperm.html', {"user": request.user})


# 主页
@login_required()
def index(request, program_name='0', program_ip='0', status='0'):
    programs = IPTVProgram.objects.all()
    # 以下为搜索功能，分别对应频道名，频道ip，状态
    if program_name != 0:
        programs = programs.filter(program_name__contains=program_name)
    if program_ip != 0:
        programs = programs.filter(program_ip__contains=program_ip)
    if status != 0:
        programs = programs.filter(status=status)
    return render(request, 'index.html', {'programs': programs})


# 关停 / 开启
def program_turn_off(request):
    if request.method == 'POST':
        try:
            mode = request.POST.get('mode')
            program_ips = request.POST.get('program_ips')
            if mode == 'turn_off':
                for ip in program_ips:
                    utils.ssh_paramiko(ip, 'root', '12', 'turn off')
            elif mode == 'turn_on':
                for ip in program_ips:
                    utils.ssh_paramiko(ip, 'root', '12', 'turn on')
            return JsonResponse({'msg': 'ok', 'code': 200})
        except Exception as e:
            print(e)
            return JsonResponse({'msg': e, 'code': 201})


# 显示操作记录
def show_log(request):
    logs = IPTVProgramOperationLog.objects.all()
    return render(request, 'program_logs.html', {'program_logs': logs})
