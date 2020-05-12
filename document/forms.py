from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from document.models import SiteUser, Passport, CourseGroup


class PassportForm(ModelForm):
    class Meta:
        model = Passport
        fields = ['Серия', 'number', 'code', 'dateTimeField', 'place']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class SiteUserForm(ModelForm):
    class Meta:
        model = SiteUser
        fields = (
            'user', 'passport', 'course_Group', 'INN', 'pFact',
            'dateBirthday', 'phoneNumber', 'patronymic', 'numberInsuranceCertificate', 'disability',
            'fullStateSupport', 'preferentialCategory', 'numberTravelCard', 'addressOfResidence', 'FormOfEducation', 'inProfCom')


class Course(ModelForm):
    class Meta:
        model = CourseGroup
        fields = ('course', 'Group', 'namePraepostor', 'nameInstitute')
