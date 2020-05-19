from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from document.models import SiteUser, Passport, CourseGroup


class PassportForm(ModelForm):
    class Meta:
        model = Passport
        fields = ['series', 'number', 'code', 'dateTimeField', 'place']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class SiteUserForm1(ModelForm):
    class Meta:
        model = SiteUser
        fields = (
            'user', 'passport', 'course_Group', 'INN', 'pFact',
            'dateBirthday', 'phoneNumber', 'inProfCom', 'patronymic', 'numberInsuranceCertificate', 'disability',
            'fullStateSupport', 'preferentialCategory', 'numberTravelCard', 'addressOfResidence', 'FormOfEducation')


class Course(ModelForm):
    class Meta:
        model = CourseGroup
        fields = ('course', 'Group', 'namePraepostor', 'nameInstitute')
