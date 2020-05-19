
import mimetypes
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from document.forms import StatementForm1
from document.models import SiteUser, Passport
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


# def info(request):
#     form0 = PassportForm()
#     form1 = UserForm()
#     form2 = SiteUserForm1()
#     form3 = Course()
#     return render(request, 'info_123.html', context={'form0': form0, 'form1': form1, 'form2': form2, 'form3': form3})


def info(request):
    form = StatementForm1()
    return render(request, 'info_123.html', context={'form': form})


def document(request):

    if request.method == "POST":
        course = request.POST['course']
        group = request.POST['group']
        doc = DocxTemplate("document/docExample/socPitanie.docx")
        context = {'course': course, 'group': group}
        doc.render(context)
        id = randint(1, 10000000)
        doc.save("document/documents/" + str(id) +".docx")

    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'index.html', context={'site_user': site_user})
    else:
        doc = DocxTemplate("document/docExample/socPitanie.docx")
        doc.save("document/documents/")
        return render(request, 'index.html')


def statements(request):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'statements.html', context={'site_user': site_user})
    else:
        return render(request, 'statements.html')


def admin(request):
    return redirect("/admin")


class UpdateProfile(UpdateView):
    model = SiteUser
    template_name = 'profile.html'
    fields = ['INN', 'pFact', 'dateBirthday', 'phoneNumber', 'patronymic', 'numberInsuranceCertificate',  'disability', 'fullStateSupport', 'preferentialCategory', 'numberTravelCard', 'addressOfResidence', 'FormOfEducation', 'inProfCom', 'passport']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['site_user'] = SiteUser.objects.get(user=self.request.user)
        return context


class UpdatePassport(UpdateView):
    model = Passport
    template_name = 'passport.html'
    fields = ['series', 'number', 'code', 'dateTimeField', 'place']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(UpdatePassport, self).get_context_data(**kwargs)
        context['site_user'] = SiteUser.objects.get(user=self.request.user)
        return context
