import mimetypes
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from document.forms import StatementForm1
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
    form = StatementForm1()
    return render(request, 'info_123.html', context={'form': form})


def document(request):
    if request.method == "POST":

        doc = DocxTemplate("document/documents/test.docx")
        name = request.POST['series']
        context = {'name': name}
        doc.render(context)
        id = randint(1, 10000000)
        doc.save("document/documents/" + str(id) + ".docx")

        excel_file_name = "document/documents/" + str(id) + ".docx"
        fp = open(excel_file_name, "rb")
        response = HttpResponse(fp.read())
        fp.close()

        file_type = mimetypes.guess_type(excel_file_name)
        if file_type is None:
            file_type = 'application/octet-stream'
        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(excel_file_name).st_size)
        response['Content-Disposition'] = "attachment; filename=document/documents/" + str(id) + ".docx"
        os.remove(excel_file_name)

        return response
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'index.html', context={'site_user': site_user})
    else:
        doc = DocxTemplate("document/documents/test.docx")
        doc.save("document/documents/test.docx")
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
    fields = ['INN', 'pFact', 'dateBirthday', 'phoneNumber', 'patronymic', 'numberInsuranceCertificate', 'disability',
              'fullStateSupport', 'preferentialCategory', 'numberTravelCard', 'addressOfResidence', 'FormOfEducation',
              'inProfCom', 'passport']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['site_user'] = SiteUser.objects.get(user=self.request.user)
        return context
