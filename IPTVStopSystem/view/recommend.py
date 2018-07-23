# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index_8(request):
    return render(request, 'recomend/recomend_8.html')


def index_9(request):
    return render(request, 'recomend/recomend_9.html')


# TODO 加载数据
def load_db(request):
    return render(request, 'recomend/recomend_9.html')


# TODO 推荐页关停
def recommend_change(request):
    return render(request, 'recomend/recomend_9.html')


