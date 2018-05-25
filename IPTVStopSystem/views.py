# coding=utf-8
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login(request):
    if request.session.get('username') is not None:
        return HttpResponseRedirect('/', {"user": request.user})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        rand = request.POST.get('rand')
        try:
            check_code = request.session['check_code']
        except Exception as e:
            print('error', e)
            check_code = ''
        # 注销session
        request.session['check_code'] = ''
        if check_code != rand:
            if request.method == "POST":
                return render(request, 'login.html', {"login_error_info": "验证码错误！"})

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect('/', {"user": request.user})
        else:
            if request.method == "POST":
                return render(request, 'login.html', {"login_error_info": "用户名或者密码错误！"})
            else:
                return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')


def noperm(request):
    return render(request, 'noperm.html', {"user": request.user})


@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')
