from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from document.models import SiteUser, Passport, CourseGroup, Statement1, DisabilityGroup, StatementProfCom1


class SiteRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',  'password1', 'password2')


class PassportForm(ModelForm):
    class Meta:
        model = Passport
        exclude = 'user',


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class SiteUserForm1(ModelForm):
    class Meta:
        model = SiteUser
        exclude = ['user', 'course_Group', 'passport']


class StatementForm6(ModelForm):
    class Meta:
        model = Statement1
        exclude = ['textfield1', 'textfield2']


class StatementForm1(ModelForm):
    class Meta:
        model = Statement1
        fields = (
            '__all__'
        )


class FormProfCom1(ModelForm):
    class Meta:
        model = StatementProfCom1
        fields = (
            '__all__'
        )


class FormProfCom23(ModelForm):
    class Meta:
        model = StatementProfCom1
        exclude = ['textfield1', 'textfield2']


class CourseForm(ModelForm):
    class Meta:
        model = CourseGroup
        fields = ('course', 'group', 'FIO_headman', 'name_institute')


class DisabilityGroupForm(ModelForm):
    class Meta:
        model = DisabilityGroup
        fields = ['categories', 'supporting_documents']
