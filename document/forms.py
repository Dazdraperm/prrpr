from django import forms
from django.contrib.auth.models import User
from document.models import SiteUser


class NameForm(forms.Form):
    class Meta:
        model = SiteUser
        fields = 'INN'
