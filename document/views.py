from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from document.forms import NameForm
from document.models import SiteUser


def index(request):
    site_user = SiteUser.objects.get(user=request.user)
    return render(request, 'index.html', context={'site_user': site_user})


def category(request):
    site_user = SiteUser.objects.get(user=request.user)
    return render(request, 'category_of_need.html', context={'site_user': site_user})


def info(request):
    site_user = SiteUser.objects.get(user=request.user)
    return render(request, 'info_123.html', context={'site_user': site_user})


def statements(request):
    site_user = SiteUser.objects.get(user=request.user)
    return render(request, 'statements.html', context={'site_user': site_user})


class UpdateProfile(UpdateView):
    model = SiteUser
    template_name = 'profile.html'
    fields = ['INN', 'pFact', 'dateBirthday', 'phoneNumber', 'patronymic', 'numberInsuranceCertificate',  'disability', 'fullStateSupport', 'preferentialCategory', 'numberTravelCard', 'addressOfResidence', 'FormOfEducation', 'inProfCom']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['site_user'] = SiteUser.objects.get(user=self.request.user)
        return context




