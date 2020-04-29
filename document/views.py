from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from document.models import SiteUser
from django.contrib.auth.models import User


def index(request):

    return render(request, 'index.html', )


def category(request):

    return render(request, 'category_of_need.html', )


def info(request):

    return render(request, 'info_123.html')


def statements(request):
    return render(request, 'statements.html')


def profile(request):
    site_user = SiteUser.objects.get(user=request.user)
    return render(request, 'profile.html', context={'site_user': site_user})


class UpdateCharacterView(UpdateView):
    model = SiteUser
    templates_name = 'profile.html'
    fields = {'INN'}
    success_url = reverse_lazy('/')

