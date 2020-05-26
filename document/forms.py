from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from document.models import SiteUser, Passport, CourseGroup, Statement1, DisabilityGroup


class SiteRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',  'password1', 'password2')


class PassportForm(ModelForm):
    class Meta:
        model = Passport
        fields = ('series', 'number', 'code', 'dateTimeField', 'placeOfRegistration', 'dateBirthday')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class SiteUserForm1(ModelForm):
    class Meta:
        model = SiteUser
        exclude = ['user', 'course_Group', 'passport']


class StatementForm1(ModelForm):
    class Meta:
        model = Statement1
        fields = (
            '__all__'
        )


class Course(ModelForm):
    class Meta:
        model = CourseGroup
        fields = ('course', 'group', 'nameHeadman', 'nameInstitute')


class DisabilityGroupForm(ModelForm):
    class Meta:
        model = DisabilityGroup
        fields = ['categories', 'documents']
