from django import forms
from document.models import SiteUser


class NameForm(forms.Form):
    class Meta:
        model = SiteUser
        fields = ('INN', 'pFact')
