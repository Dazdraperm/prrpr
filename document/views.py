from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from document.models import SiteUser
from docxtpl import DocxTemplate
from random import randint


def index(request):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'index.html', context={'site_user': site_user})
    else:
        return render(request, 'index.html')


def category(request):
    site_user = SiteUser.objects.get(user=request.user)
    return render(request, 'category_of_need.html', context={'site_user': site_user})


def info(request):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'info_123.html', context={'site_user': site_user})
    else:
        return render(request, 'info_123.html')


def document(request):
    site_user = SiteUser.objects.get(user=request.user)
    name = site_user.passport.series
    passport = site_user.passport.series
    doc = DocxTemplate("document/test.docx")
    context = {'name': name, 'nomer': passport}
    doc.render(context)
    # document = Document('test.docx')
    # document.save('example.docx')
    id = randint(1, 10000000)
    doc.save("document/documents/" + str(id) +".docx")
    return render(request, 'index.html', context={'site_user': site_user})


def statements(request):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'statements.html', context={'site_user': site_user})
    else:
        return render(request, 'statements.html')


class UpdateProfile(UpdateView):
    model = SiteUser
    template_name = 'profile.html'
    fields = ['INN', 'pFact', 'dateBirthday', 'phoneNumber', 'patronymic', 'numberInsuranceCertificate',  'disability', 'fullStateSupport', 'preferentialCategory', 'numberTravelCard', 'addressOfResidence', 'FormOfEducation', 'inProfCom']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['site_user'] = SiteUser.objects.get(user=self.request.user)
        return context




