from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_Last_name = forms.CharField(label='Your name', max_length=100)
    your_Data = forms.CharField(label='Your name', max_length=100)
