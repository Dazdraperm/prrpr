from django.shortcuts import render
from django.http import HttpResponseRedirect

from document.forms import NameForm


def index(request):
    return render(request, 'index.html')


def category(request):
    return render(request, 'category_of_need.html')


def get_name(request):
    if request.method == "POST":
        return HttpResponseRedirect('/')


def info(request):
    return render(request, 'info_123.html')


def statements(request):
    return render(request, 'statements.html')
