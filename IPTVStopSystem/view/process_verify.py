from django.shortcuts import render

from IPTVStopSystem.models import IPTVProcessVerify


def show_process_verify(request):
    verifies = IPTVProcessVerify.objects.all()
    return render(request, 'process_verify.html', {'verifies': verifies})


def process_pass(request, process):
    process_type = process.operation_type
    if process_type == 1:
        pass
    elif process_type == 2:
        pass
    elif process_type == 3:
        pass


def process_reject(request, process):
    process_type = process.operation_type
    if process_type == 1:
        pass
    elif process_type == 2:
        pass
    elif process_type == 3:
        pass


def process_verify(request):
    if request.method == 'POST':
        mode = request.POST.get('mode')
        process_id = request.POST.get('process_id')
        process = IPTVProcessVerify.objects.get(id=process_id)
        if mode == 'pass':
            return process_pass(request, process)
        elif mode == 'reject':
            return process_reject(request, process)
