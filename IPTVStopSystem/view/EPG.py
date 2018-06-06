# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from IPTVStopSystem import utils


@login_required()
def show_epg(request):
    return render(request, 'epg/epg.html')


@login_required()
def epg_one_key(request):
    if request.method == 'POST':
        pass
