from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from document.models import SiteUser


def index(request):
    site_user = SiteUser.objects.get(user=request.user)
    return render(request, 'index.html', context={'site_user': site_user})


def category(request):

    return render(request, 'category_of_need.html', )


def info(request):

    return render(request, 'info_123.html')


def statements(request):
    return render(request, 'statements.html')


class UpdateProfile(UpdateView):
    model = SiteUser
    template_name = 'profile.html'
    fields = ['INN', 'pFact']
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['site_user'] = SiteUser.objects.get(user=self.request.user)
        return context




