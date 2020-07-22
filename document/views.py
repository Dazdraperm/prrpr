import mimetypes
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from document.forms import SiteRegistrationForm, StatementForm6, FormProfCom1, FormProfCom23
from document.forms import StatementForm1, SiteUserForm1, PassportForm, CourseForm
from document.models import SiteUser, CourseGroup, Passport
from docxtpl import DocxTemplate


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SiteRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('my_login')
            else:
                return redirect('is_not_valid')
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


def is_not_valid(request):
    return render(request, 'registration/is_not_valid.html')


def schedule(request):
    return render(request, 'schedule.html')


def consent(request):
    return render(request, 'statements/first_7/info_6/info_6_links/consent.html')


def contract(request):
    return render(request, 'statements/first_7/info_6/info_6_links/contract.html')


def material_aid(request, pk):
    form = FormProfCom1
    return render(request, 'statements/last_123/material_aid/material_aid.html', context={'form': form, 'pk': pk})


def online_wallet(request, pk):
    form = FormProfCom23
    return render(request, 'statements/last_123/online_wallet/online_wallet.html', context={'form': form, 'pk': pk})


def social_nutrition(request, pk):
    form = FormProfCom23
    return render(request, 'statements/last_123/social_nutrition/social_nutrition.html',
                  context={'form': form, 'pk': pk})


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
        form = StatementForm6(initial={'number_of_statement': pk})
        return render(request, 'statements/first_7/info_6/info_6.html', context={'form': form, 'pk': pk}, )
    else:
        form = StatementForm1(initial={'number_of_statement': pk})
    return render(request, 'statements/first_7/info_123/info_123.html', context={'form': form, 'pk': pk}, )


def position(request):
    return render(request, 'statements/first_7/conditions/position/position.html')


def how(request):
    return render(request, 'statements/last_123/how.html')


def auto_fill(request, pk):
    if request.user.is_authenticated:
        site_user = SiteUser.objects.get(user=request.user)
        course_group = CourseGroup.objects.get(user=request.user)
        passport = Passport.objects.get(user=request.user)
        if pk in range(1, 8):
            print(pk + pk)
            form = StatementForm1(initial={
                # Юзер
                'name': site_user.name,
                'surname': site_user.surname,

                # Пасспорт
                'unit_code': passport.unit_code,
                'series': passport.series,
                'number_passport': passport.number_passport,
                'date_birthday': passport.date_birthday,
                'place_registration': passport.place_registration,
                'passport_issue_day': passport.passport_issue_day,
                'passport_issue_month': passport.passport_issue_month,
                'passport_issue_year': passport.passport_issue_year,

                # Курс и группа
                'course': course_group.course,
                'name_institute': course_group.course,
                'group': course_group.group,
                'FIO_headman': course_group.FIO_headman,
                'pk': pk,

                # Сайт юзер
                'INN': site_user.INN,
                'location_street': site_user.location_street,
                'location_house': site_user.location_house,
                'post_code': site_user.post_code,
                'location_apartment': site_user.location_apartment,
                'phone_number': site_user.phone_number,
                'patronymic': site_user.patronymic,
                'number_insurance_certificate': site_user.number_insurance_certificate,
                'disability_group': site_user.disability_group,
                'full_state_support': site_user.full_state_support,
                'number_travel_card': site_user.number_travel_card,
                'state_prof_com': site_user.state_prof_com,
            })
            if pk == 6:
                return render(request, 'statements/first_7/info_6/info_6.html', context={'form': form, 'pk': pk})
            else:
                return render(request, 'statements/first_7/info_123/info_123.html', context={'form': form, 'pk': pk})

        if pk in range(8, 11):
            print(pk)
            form = FormProfCom1(initial={
                # Здесь начинаются поля Юзера
                'name': site_user.name,
                'surname': site_user.surname,

                # Здес начинаются поля Пасспорта
                'series': passport.series,
                'number_passport': passport.number_passport,
                'date_birthday': passport.date_birthday,
                'place_registration': passport.place_registration,

                # Здесь начинаются поля Курса и группы
                'name_institute': course_group.name_institute,
                'group': course_group.group,

                # Здесь начинаются поля Сайт юзера
                'INN': site_user.INN,
                'location_apartment': site_user.location_apartment,
                'house': site_user.location_house,
                'location_street': site_user.location_street,
                'phone_number': site_user.phone_number,
                'patronymic': site_user.patronymic,
                'number_insurance_certificate': site_user.number_insurance_certificate,
                'disability_group': site_user.disability_group,
                'full_state_support': site_user.full_state_support,
                'number_travel_card': site_user.number_travel_card,
                'state_prof_com': site_user.state_prof_com, })
            if pk == 8:
                return render(request, 'statements/last_123/material_aid/material_aid.html', context={'form': form, 'pk': pk})
            elif pk == 9:
                return render(request, 'statements/last_123/online_wallet/online_wallet.html', context={'form': form, 'pk': pk}) 
            elif pk == 10:
                return render(request, 'statements/last_123/social_nutrition/social_nutrition.html',
                              context={'form': form, 'pk': pk})
    else:
        return render(request, 'index.html')


def doc_budget_soc(request, pk):
    if request.method == "POST":
        doc = DocxTemplate("document/docExample/doc_budget_soc.docx")
        context = {
            # Курс
            "c": request.POST['course'],
            "group": request.POST['group'],
            'FIO_headman': request.POST['FIO_headman'],
            'name_institute': request.POST['name_institute'],

            # Паспорт
            'series': request.POST['series'],
            'number': request.POST['number_passport'],
            'issued_passport': request.POST['issued_passport'],
            'date_birthday': request.POST['date_birthday'],
            'passport_issue_day': request.POST['passport_issue_day'],
            'passport_issue_month': request.POST['passport_issue_month'],
            'passport_issue_year': request.POST['passport_issue_year'],

            # Основные данные
            'phone_number': request.POST['phone_number'],
            'INN': request.POST['INN'],
            'location_apartment': request.POST['location_apartment'],
            'location_house': request.POST['location_house'],
            'location_street': request.POST['location_street'],
            'number_insurance_certificate': request.POST['number_insurance_certificate'],
            'disability_group': request.POST['disability_group'],
            'full_state_support': request.POST['full_state_support'],
            'surname': request.POST['surname'],
            'name': request.POST['name'],
            'post_code': request.POST['post_code'],
            'patronymic': request.POST['patronymic'],

            'pk': pk}

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


def doc_budget_main(request, pk):
    if request.method == "POST":
        doc = DocxTemplate("document/docExample/doc_budget_main.docx")

        context = {
            # Основные
            'phone_number': request.POST['phone_number'],
            'INN': request.POST['INN'],
            'location_apartment': request.POST['location_apartment'],
            'location_house': request.POST['location_house'],
            'location_street': request.POST['location_street'],
            'number_insurance_certificate': request.POST['number_insurance_certificate'],
            'disability_group': request.POST['disability_group'],
            'full_state_support': request.POST['full_state_support'],
            'surname': request.POST['surname'],
            'name': request.POST['name'],
            'post_code': request.POST['post_code'],
            'patronymic': request.POST['patronymic'],

            # Курс
            "c": request.POST['course'],
            "group": request.POST['group'],
            'FIO_headman': request.POST['FIO_headman'],
            'name_institute': request.POST['name_institute'],

            # Паспорт
            'series': request.POST['series'],
            'number': request.POST['number_passport'],
            'issued_passport': request.POST['issued_passport'],
            'date_birthday': request.POST['date_birthday'],
            'passport_issue_day': request.POST['passport_issue_day'],
            'passport_issue_month': request.POST['passport_issue_month'],
            'passport_issue_year': request.POST['passport_issue_year'],

            # Уникальные
            "request": request.POST['request'],
            "annex": request.POST['annex'],
            'pk': pk}
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


def doc_profcom_2(request, pk):
    if request.method == "POST":
        doc = DocxTemplate("document/docExample/doc_profcom_2.docx")  # или должен сохранять 3
        context = {
            # Курс
            "group": request.POST['group'],
            'name_institute': request.POST['name_institute'],

            # Паспорт
            'series': request.POST['series'],
            'number': request.POST['number_passport'],
            'issued_passport': request.POST['issued_passport'],
            'date_birthday': request.POST['date_birthday'],
            'passport_issue_day': request.POST['passport_issue_day'],
            'passport_issue_month': request.POST['passport_issue_month'],
            'passport_issue_year': request.POST['passport_issue_year'],

            # Основа
            "INN": request.POST['INN'],
            "number_phone": request.POST['phone_number'],
            'surname': request.POST['surname'],
            'name': request.POST['name'],
            'post_code': request.POST['post_code'],
            'patronymic': request.POST['patronymic'],
            'location_apartment': request.POST['location_apartment'],
            'location_house': request.POST['location_house'],
            'location_street': request.POST['location_street']}
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


def doc_profcom_1(request, pk):
    if request.method == "POST":
        doc = DocxTemplate("document/docExample/doc_profcom_1.docx")
        context = {
            # Курс
            "group": request.POST['group'],
            'name_institute': request.POST['name_institute'],

            # Паспорт
            'series': request.POST['series'],
            'number': request.POST['number_passport'],
            'issued_passport': request.POST['issued_passport'],
            'date_birthday': request.POST['date_birthday'],
            'passport_issue_day': request.POST['passport_issue_day'],
            'passport_issue_month': request.POST['passport_issue_month'],
            'passport_issue_year': request.POST['passport_issue_year'],

            # Основа
            "INN": request.POST['INN'],
            "number_phone": request.POST['phone_number'],
            'surname': request.POST['surname'],
            'name': request.POST['name'],
            'patronymic': request.POST['patronymic'],
            'location_apartment': request.POST['location_apartment'],
            'location_house': request.POST['location_house'],
            'location_street': request.POST['location_street'],

            # Уникальные
            "request": request.POST['request'],
            "annex": request.POST['annex']}
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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/")
        return super(UpdateProfile, self).dispatch(request, *args, **kwargs)

    model = SiteUser
    template_name = 'profile_list/profile.html'
    form_class = SiteUserForm1
    success_url = reverse_lazy('profile')


    # def get_context_data(self, **kwargs):
    #     site_user = SiteUser.objects.get(user=self.request.user)
    #     context = super(UpdateProfile, self).get_context_data(**kwargs)
    #     context['active_client'] = True
    #     # if 'form' not in context:
    #     context['form'] = self.form_class(initial={'INN': site_user.INN,
    #                                                'location_street': site_user.location_street,
    #                                                'post_code': site_user.post_code,
    #                                                'location_house': site_user.location_house,
    #                                                'name': site_user.name,
    #                                                'surname': site_user.surname,
    #                                                'location_apartment': site_user.location_apartment,
    #                                                'phone_number': site_user.phone_number,
    #                                                'patronymic': site_user.patronymic,
    #                                                'numberInsuranceCertificate': site_user.number_insurance_certificate,
    #                                                'disability_group': site_user.disability_group,
    #                                                'full_state_support': site_user.full_state_support,
    #                                                'number_travel_card': site_user.number_travel_card,
    #                                                'state_prof_com': site_user.state_prof_com})
    #
    #     context['active_client'] = True
    #     return context


class UpdateCourse(UpdateView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/")
        return super(UpdateCourse, self).dispatch(request, *args, **kwargs)

    model = CourseGroup
    template_name = 'profile_list/course_group.html'
    form_class = CourseForm
    success_url = reverse_lazy('course_group')


    # def get_context_data(self, **kwargs):
    #     course_group = CourseGroup.objects.get(user=self.request.user)
    #     context = super(UpdateCourse, self).get_context_data(**kwargs)
    #     context['active_client'] = True
    #     print(course_group.course)
    #     print(course_group.FIO_headman)
    #     print(course_group.name_institute)
    #     context['form'] = self.form_class(initial={'course': course_group.course,
    #                                                'name_institute': course_group.name_institute,
    #                                                'group': course_group.group,
    #                                                'FIO_headman': course_group.FIO_headman})
    #     context['active_client'] = True
    #     return context


class UpdatePassport(UpdateView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/")
        return super(UpdatePassport, self).dispatch(request, *args, **kwargs)

    model = Passport
    template_name = 'profile_list/passport.html'
    form_class = PassportForm
    success_url = reverse_lazy('passport')


    # def get_context_data(self, **kwargs):
    #     passport = Passport.objects.get(user=self.request.user)
    #     context = super(UpdatePassport, self).get_context_data(**kwargs)
    #     context['active_client'] = True
    #     context['form'] = self.form_class(initial={'unit_code': passport.unit_code,
    #                                                'series': passport.series,
    #                                                'number_passport': passport.number_passport,
    #                                                'date_birthday': passport.date_birthday,
    #                                                'place_registration': passport.place_registration,
    #                                                'passport_issue_day': passport.passport_issue_day,
    #                                                'passport_issue_month': passport.passport_issue_month,
    #                                                'passport_issue_year': passport.passport_issue_year,
    #                                                'issued_passport': passport.issued_passport})
    #     context['active_client'] = True
    #     return context


def my_logout(request):
    return redirect('accounts/logout')


def my_login(request):
    return redirect('accounts/login')


def my_reset_password(request):
    return redirect('accounts/re')
