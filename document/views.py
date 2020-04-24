from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    x = request.user.email
    if x[::-12] == 'stud.kpfu.ru':
        return render(request, 'index3.html')

    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'index2.HTML')
