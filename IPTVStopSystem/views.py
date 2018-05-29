# coding=utf-8
import time
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from models import IPTVProgram
from models import IPTVProgramOperationLog
import utils


# 登录验证
def login(request):
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            print('already login')
            return redirect('/')
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        # print('session', request.session.get('username'))
        # if request.session.get('username') is not None:
        #     return HttpResponseRedirect('/', {"user": request.user})
        # else:
        #     username = request.POST.get('username')
        #     password = request.POST.get('password')
        #     print('username', username)
        #     print('password', password)
        #     user = auth.authenticate(username=username, password=password)
        #     if user and user.is_active:
        #         auth.login(request, user)
        #         request.session['username'] = username
        #         return HttpResponseRedirect('/', {"user": request.user})
        #     return render(request, 'login.html', {"login_error_info": "用户名或者密码错误！"})
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print('username', username)
        print('username', password)
        if user is not None and user.is_active:
            auth.login(request, user)
            # 更新最后登录时间
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            user.last_login = now_time
            user.save()
            return redirect('/', {"user": request.user})
        else:
            return render(request, 'login.html', {'error': '邮箱或者密码不正确'})


# 登录
def logout(request):
    auth.logout(request)
    return redirect('/login')


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
    # programs.program_name 频道名称
    # programs.program_desc 频道描述
    # programs.router 控制路由组
    # programs.program_ip 频道ip
    # programs.status 频道状态
    # programs.strategy 策略id
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
