from django.shortcuts import render

from document.forms import NameForm


def index(request):
    form = NameForm
    return render(request, 'index.html', context={'form': form})


def category(request):
    return render(request, 'category_of_need.html')


def info(request):
    return render(request, 'info_123.html')


def statements(request):
    return render(request, 'statements.html')
