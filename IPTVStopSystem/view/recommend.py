from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index_8(request):
    return render(request, 'recomend/recomend_8.html')


def index_9(request):
    return render(request, 'recomend/recomend_9.html')