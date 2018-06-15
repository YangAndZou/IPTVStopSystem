# coding=utf-8
import random
import string
import time
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect


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
            rand = request.POST.get('rand')
            try:
                check_code = request.session['check_code']
            except:
                check_code = ''
            if check_code != rand:
                if request.method == "POST":
                    return JsonResponse({"status": "验证码错误"})
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                request.session['check_code'] = ''
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


@login_required()
def redirect_to_index(request):
    if request.user.is_superuser:
        return redirect('/index')
    else:
        return redirect('/process_verify')


def create_code_img(request):
    # 在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    # 创建图片，模式，大小，背景色
    img = Image.new('RGB', (120, 30), (255, 255, 255))
    # 创建画布
    draw = ImageDraw.Draw(img)
    # 设置字体
    font = ImageFont.truetype('Arial.ttf', 25)

    code = getRandomChar()
    # 将生成的字符画在画布上
    for t in range(4):
        draw.text((30 * t + 5, 0), code[t], getRandomColor(), font)

    # 生成干扰点
    for _ in range(random.randint(0, 150)):
        # 位置，颜色
        draw.point((random.randint(0, 120), random.randint(0, 30)), fill=getRandomColor())

    # 使用模糊滤镜使图片模糊
    # img = img.filter(ImageFilter.BLUR)

    request.session['check_code'] = code
    img.save(f, 'gif')
    return HttpResponse(f.getvalue(), 'image/gif')


# 生成随机字符串
def getRandomChar():
    # string模块包含各种字符串，以下为小写字母加数字
    ran = string.ascii_lowercase + string.digits
    char = ''
    for i in range(4):
        char += random.choice(ran)
    return char


# 返回一个随机的RGB颜色
def getRandomColor():
    return (random.randint(50, 150),
            random.randint(50, 150), random.randint(50, 150))
