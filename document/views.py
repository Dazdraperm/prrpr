import mimetypes
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from document.forms import StatementForm1
from document.models import SiteUser, Passport
from docxtpl import DocxTemplate


def index(request):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'index.html', context={'site_user': site_user})
    else:
        return render(request, 'index.html')


def category(request):
    return render(request, 'category_of_need.html')


def info(request):
    form = StatementForm1()
    return render(request, 'info_123.html', context={'form': form})


def login(request):
    return redirect('accounts/login')

#def auto_fill(request):
 #   if request.method == "POST":



def document(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            id = request.user.last_name
            doc = DocxTemplate("document/documents/test.docx")
            context = {}
            doc.render(context)
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
            response['Content-Disposition'] = "attachment; filename= " + str(id) + ".docx"
            os.remove(excel_file_name)
            return response
        else:
            doc = DocxTemplate("document/documents/test.docx")
            context = {}
            doc.render(context)
            doc.save("document/documents/anonym.docx")

            excel_file_name = "document/documents/anonym.docx"
            fp = open(excel_file_name, "rb")
            response = HttpResponse(fp.read())
            fp.close()

            file_type = mimetypes.guess_type(excel_file_name)
            if file_type is None:
                file_type = 'application/octet-stream'
            response['Content-Type'] = file_type
            response['Content-Length'] = str(os.stat(excel_file_name).st_size)
            response['Content-Disposition'] = "attachment; filename= anonym.docx"
            os.remove(excel_file_name)
            return response


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


class UpdatePassport(UpdateView):
    model = Passport
    template_name = 'passport.html'
    fields = ['series', 'number', 'code', 'dateTimeField', 'place']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(UpdatePassport, self).get_context_data(**kwargs)
        context['site_user'] = SiteUser.objects.get(user=self.request.user)
        return context
