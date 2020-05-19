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


def login(request):
    return redirect('accounts/login')


def document(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            id = request.user.last_name
            doc = DocxTemplate("document/docExample/socPitanie.docx")
            course = request.POST['course']
            group = request.POST['group']
            context = {"group": group, "course": course}
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
            doc = DocxTemplate("document/docExample/socPitanie.docx")
            doc = DocxTemplate("document/docExample/socPitanie.docx")
            course = request.POST['course']
            group = request.POST['group']
            nameHeadman = request.POST['nameHeadman']
            name_institute = request.POST['name_institute']
            series = request.POST['series']
            number = request.POST['number']
            code = request.POST['code']
            dateTimeField = request.POST['dateTimeField']
            INN = request.POST['INN']
            place = request.POST['place']
            dateBirthday = request.POST['dateBirthday']
            numberPhone = request.POST['phoneNumber']
            certificate = request.POST['numberInsuranceCertificate']
            dateBirthday = request.POST['dateBirthday']
            pFact = request.POST['pFact']
            invalid = request.POST['disability_group']
            invalid2 = request.POST['disability_group_text']
            answer = request.POST['fullStateSupport']
            surname = request.POST['surname']
            name = request.POST['name']
            patronymic = request.POST['patronymic']

            context = {"group": group, "course": course, "starosta": nameHeadman, "name": name_institute,
                       "nomer": number, "series": series,  "vidan": place, "inn": INN, "adress": pFact,
                        "svidetel": certificate, "dateNumber": dateBirthday, "invalid": invalid, "invalid2": invalid2,
                       "answer": answer, "numberPhone": numberPhone, "sur": surname, "nam": name, "otchet": patronymic}
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
