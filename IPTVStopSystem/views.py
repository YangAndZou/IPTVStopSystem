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
        return render(request, 'login.html')
    elif request.method == 'POST':
        print('session', request.session.get('username'))
        # session不为空，无需再次登录
        if request.session.get('username') is not None:
            return redirect('/', {"user": request.user})
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # 存储session
                request.session['username'] = username
                now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                user.last_login = now_time
                user.save()
                return redirect('/', {"user": request.user})
            return render(request, 'login.html', {"login_error_info": "用户名或者密码错误！"})


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
    if request.method == 'GET':
        programs = IPTVProgram.objects.all()
        # 以下为搜索功能，分别对应频道名，频道ip，状态
        if program_name != '0':
            programs = programs.filter(program_name=program_name)
        if program_ip != '0':
            programs = programs.filter(program_ip__contains=program_ip)
        if status != '0':
            programs = programs.filter(status=status)
        return render(request, 'directBroadcast.html', {'programs': programs})
