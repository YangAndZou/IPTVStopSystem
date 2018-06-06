# coding=utf-8
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from IPTVStopSystem import utils


def show_epg(request):
    return render(request, 'epg/epg.html')


def epg_one_key(request):
    if request.method == 'POST':
        pass
