# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from utils import utils


@login_required
def index_8(request):
    return render(request, 'recomend/recomend_8.html')


@login_required
def index_9(request):
    return render(request, 'recomend/recomend_9.html')


# TODO 加载数据
@login_required
def load_db(request):
    return render(request, 'recomend/recomend_9.html')


@login_required
def recommend_change_8(request):
    position_head = request.POST.get('position_head')
    position = request.POST.get('position')
    status = request.POST.get('status')

    try:
        if position is None and position_head is None:
            return JsonResponse({'code': 500, 'msg': '无效的坐标！'})

        # 0表示关停状态，需要开启
        if status == '0':
            utils.turn_on(position_head, position)
            return JsonResponse({'code': 200, 'msg': '开启成功！'})
        else:
            utils.turn_off(position_head, position)
            return JsonResponse({'code': 200, 'msg': '关停成功！'})

    except Exception as e:
        return JsonResponse({'code': 500, 'msg': e})






