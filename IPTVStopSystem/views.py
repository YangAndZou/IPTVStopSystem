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
        # session不为空，无需再次登录
        if request.session.get('username') is not None:
            return JsonResponse({"status": "ok"})
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
                return JsonResponse({"status": "ok"})
            return JsonResponse({"status": "用户名或者密码错误！"})


# 登录
def logout(request):
    auth.logout(request)
    return redirect('/login')


# 用户没有权限时触发
def noperm(request):
    return render(request, 'noperm.html', {"user": request.user})


# 主页
@login_required()
def index(request):
    if request.user.username == 'admin':
        return render(request, 'admin.html')
    else:
        return render(request, 'epg/epg.html')


def redirect_to_index(request):
    return redirect('/index')

