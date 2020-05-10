from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from document.models import SiteUser, Passport


class NameForm(ModelForm):
    class Meta:
        model = Passport
        fields = ['series', 'number']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
