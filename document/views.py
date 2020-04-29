from django.shortcuts import render

from document.models import SiteUser


def index(request):

    return render(request, 'index.html', )


def category(request):

    return render(request, 'category_of_need.html', )


def info(request):

    return render(request, 'info_123.html')


def statements(request):
    return render(request, 'statements.html')


def profile(request):
    user = SiteUser.objects.get(user=request.user)
    return render(request, 'profile.html', context={'user': user})


