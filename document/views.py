import mimetypes
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from document.forms import SiteRegistrationForm
from document.forms import StatementForm1, SiteUserForm1, PassportForm, Course
from document.models import SiteUser, CourseGroup, Passport
from docxtpl import DocxTemplate


def register(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            form = SiteRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('index')
        else:
            form = SiteRegistrationForm()
            return render(request, 'registration/register.html', {'form': form})
    else:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'index.html', context={'site_user': site_user})


def index(request):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        return render(request, 'index.html', context={'site_user': site_user})
    else:
        return render(request, 'index.html')


def schedule(request):
    return render(request, 'schedule.html')


def consent(request):
    return render(request, 'statements/first_7/info_6/info_6_links/consent.html')


def contract(request):
    return render(request, 'statements/first_7/info_6/info_6_links/contract.html')


def material_aid(request):
    form = StatementForm1
    return render(request, 'statements/last_123/material_aid/material_aid.html', context={'form': form})


def online_wallet(request):
    form = StatementForm1
    return render(request, 'statements/last_123/online_wallet/online_wallet.html', context={'form': form})


def social_nutrition(request):
    form = StatementForm1
    return render(request, 'statements/last_123/social_nutrition/social_nutrition.html', context={'form': form})


def survey_questionnaire(request):
    return render(request, 'statements/first_7/info_6/info_6_links/survey_questionnaire.html')


def additional_bank(request):
    return render(request, 'statements/first_7/info_6/info_6_links/additional_bank.html')


def statement_of_command(request):
    return render(request, 'statements/first_7/info_6/info_6_links/statement_of_command.html')


def conditions(request):
    return render(request, 'statements/first_7/conditions/conditions.html')


def category(request):
    return render(request, 'statements/category_of_need.html')


def informer(request):
    return render(request, 'statements/first_7/info_123/informers/informer_4.html')


def info(request, pk):
    if pk == 6:
        form = StatementForm1()
        return render(request, 'statements/first_7/info_6/info_6.html', context={'form': form, 'pk': pk}, )
    else:
        form = StatementForm1()
    return render(request, 'statements/first_7/info_123/info_123.html', context={'form': form, 'pk': pk}, )


def position(request):
    return render(request, 'statements/first_7/conditions/position/position.html')


def my_login(request):
    return redirect('accounts/login')


def how(request):
    return render(request, 'statements/last_123/how.html')


def auto_fill(request, pk):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        if site_user.passport is None:
            course_group = CourseGroup.objects.get(user=request.user)
            form = StatementForm1(initial={
                # Здесь начинаются поля Юзера
                'name': request.user.first_name,
                'surname': request.user.last_name,

                # Здесь начинаются поля Курса и группы
                'course': course_group.course,
                'name_institute': course_group.course,
                'group': course_group.group,
                'nameHeadman': course_group.nameHeadman,

                # Здесь начинаются поля Сайт юзера
                'INN': site_user.INN,
                'pFact': site_user.pFact,
                'phoneNumber': site_user.phoneNumber,
                'patronymic': site_user.patronymic,
                'numberInsuranceCertificate': site_user.numberInsuranceCertificate,
                'disability': site_user.disability,
                'fullStateSupport': site_user.fullStateSupport,
                'preferentialCategory': site_user.preferentialCategory,
                'numberTravelCard': site_user.numberTravelCard,
                'addressOfResidence': site_user.addressOfResidence,
                'FormOfEducation': site_user.FormOfEducation,
                'inProfCom': site_user.inProfCom,
            })
            return render(request, 'statements/first_7/info_123/info_123.html', context={'form': form})
        elif site_user.course_Group is None:

            passport = Passport.objects.get(user=request.user)
            form = StatementForm1(initial={
                # Здесь начинаются поля Юзера
                'name': request.user.first_name,
                'surname': request.user.last_name,

                # Здес начинаются поля Пасспорта
                'code': passport.code,
                'series': passport.series,
                'number': passport.number,
                'dateBirthday': passport.dateBirthday,
                'place': passport.placeOfRegistration,
                'dateTimeField': passport.dateTimeField,

                # Здесь начинаются поля Сайт юзера
                'INN': site_user.INN,
                'pFact': site_user.pFact,
                'phoneNumber': site_user.phoneNumber,
                'patronymic': site_user.patronymic,
                'numberInsuranceCertificate': site_user.numberInsuranceCertificate,
                'disability': site_user.disability,
                'fullStateSupport': site_user.fullStateSupport,
                'preferentialCategory': site_user.preferentialCategory,
                'numberTravelCard': site_user.numberTravelCard,
                'addressOfResidence': site_user.addressOfResidence,
                'FormOfEducation': site_user.FormOfEducation,
                'inProfCom': site_user.inProfCom,
            })
            return render(request, 'statements/first_7/info_123/info_123.html', context={'form': form})
        else:
            course_group = CourseGroup.objects.get(user=request.user)
            passport = Passport.objects.get(user=request.user)
            form = StatementForm1(initial={
                # Здесь начинаются поля Юзера
                'name': request.user.first_name,
                'surname': request.user.last_name,

                # Здес начинаются поля Пасспорта
                'code': passport.code,
                'series': passport.series,
                'number': passport.number,
                'dateBirthday': passport.dateBirthday,
                'place': passport.placeOfRegistration,
                'dateTimeField': passport.dateTimeField,

                # Здесь начинаются поля Курса и группы
                'course': course_group.course,
                'name_institute': course_group.course,
                'group': course_group.group,
                'nameHeadman': course_group.nameHeadman,

                # Здесь начинаются поля Сайт юзера
                'INN': site_user.INN,
                'pFact': site_user.pFact,
                'phoneNumber': site_user.phoneNumber,
                'patronymic': site_user.patronymic,
                'numberInsuranceCertificate': site_user.numberInsuranceCertificate,
                'disability': site_user.disability,
                'fullStateSupport': site_user.fullStateSupport,
                'preferentialCategory': site_user.preferentialCategory,
                'numberTravelCard': site_user.numberTravelCard,
                'addressOfResidence': site_user.addressOfResidence,
                'FormOfEducation': site_user.FormOfEducation,
                'inProfCom': site_user.inProfCom,
            })
            return render(request, 'statements/first_7/info_123/info_123.html', context={'form': form})
    else:
        return render(request, 'index.html')


def document(request, pk):
    if request.method == "POST":
        doc = DocxTemplate("document/docExample/socPitanie.docx")
        course = request.POST['course']
        group = request.POST['group']
        nameHeadman = request.POST['nameHeadman']
        name_institute = request.POST['name_institute']
        series = request.POST['series']
        number = request.POST['number']
        INN = request.POST['INN']
        place = request.POST['place']
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
                   "nomer": number, "series": series, "vidan": place, "inn": INN, "adress": pFact,
                   "svidetel": certificate, "dateNumber": dateBirthday, "invalid": invalid, "invalid2": invalid2,
                   "answer": answer, "numberPhone": numberPhone, "sur": surname, "nam": name, "otchet": patronymic}
        doc.render(context)
        doc.save("document/documents/Soc.docx")

        excel_file_name = "document/documents/Soc.docx"
        fp = open(excel_file_name, "rb")
        response = HttpResponse(fp.read())
        fp.close()

        file_type = mimetypes.guess_type(excel_file_name)
        if file_type is None:
            file_type = 'application/octet-stream'
        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(excel_file_name).st_size)
        response['Content-Disposition'] = "attachment; filename= Soc.docx"
        os.remove(excel_file_name)
        return response


def statements(request):
    return render(request, 'statements/statements.html')


def admin(request):
    return redirect("/admin")


class UpdateProfile(UpdateView):
    model = SiteUser
    template_name = 'profile_list/profile.html'
    form_class = SiteUserForm1
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        site_user = SiteUser.objects.get(user=self.request.user)
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['active_client'] = True
        # if 'form' not in context:
        context['form'] = self.form_class(initial={'INN': site_user.INN,
                                                   'pFact': site_user.pFact,
                                                   'phoneNumber': site_user.phoneNumber,
                                                   'patronymic': site_user.patronymic,
                                                   'numberInsuranceCertificate': site_user.numberInsuranceCertificate,
                                                   'disability': site_user.disability,
                                                   'fullStateSupport': site_user.fullStateSupport,
                                                   'preferentialCategory': site_user.preferentialCategory,
                                                   'numberTravelCard': site_user.numberTravelCard,
                                                   'addressOfResidence': site_user.addressOfResidence,
                                                   'FormOfEducation': site_user.FormOfEducation,
                                                   'inProfCom': site_user.inProfCom})

        context['active_client'] = True
        return context


class UpdateCourse(UpdateView):
    model = CourseGroup
    template_name = 'profile_list/course_group.html'
    form_class = Course
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        course_group = CourseGroup.objects.get(user=self.request.user)
        context = super(UpdateCourse, self).get_context_data(**kwargs)
        context['active_client'] = True
        context['form'] = self.form_class(initial={'course': course_group.course,
                                                   'nameInstitute': course_group.nameInstitute,
                                                   'group': course_group.group,
                                                   'nameHeadman': course_group.nameHeadman, })
        context['active_client'] = True
        return context


class UpdatePassport(UpdateView):
    model = Passport
    template_name = 'profile_list/passport.html'
    form_class = PassportForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        passport = Passport.objects.get(user=self.request.user)
        context = super(UpdatePassport, self).get_context_data(**kwargs)
        context['active_client'] = True
        context['form'] = self.form_class(initial={'code': passport.code,
                                                   'series': passport.series,
                                                   'number': passport.number,
                                                   'dateBirthday': passport.dateBirthday,
                                                   'placeOfRegistration': passport.placeOfRegistration,
                                                   'dateTimeField': passport.dateTimeField, })
        context['active_client'] = True
        return context


def my_logout(request):
    redirect('accounts/logout')
