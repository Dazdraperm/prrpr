from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from document.forms import NameForm, UserForm, Course
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


def info(request):
    form = NameForm()
    form1 = UserForm()
    form2 = SiteUser()
    form3 = Course()
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'info_123.html', context={'site_user': site_user, 'form': form, 'form1': form1, 'form2': form2, 'form3': form3})
    else:
        return render(request, 'info_123.html')


def document(request):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        if request.method == "POST":
            series = request.POST['username']

            doc = DocxTemplate("document/documents/test.docx")
            context = {'series': series}
            doc.render(context)
            id = randint(1, 10000000)
            doc.save("document/documents/" + str(id) +".docx")
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
