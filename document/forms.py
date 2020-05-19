from django.contrib.auth.models import User
from django.forms import ModelForm

from document.models import SiteUser, Passport, CourseGroup, Statement1, DisabilityGroup


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
            'INN', 'pFact', 'dateBirthday', 'phoneNumber', 'inProfCom', 'patronymic', 'numberInsuranceCertificate',
            'disability', 'fullStateSupport', 'preferentialCategory', 'numberTravelCard', 'addressOfResidence',
            'FormOfEducation'
        )


class StatementForm1(ModelForm):
    class Meta:
        model = Statement1
        fields = (
            'course', 'group', 'nameHeadman', 'nameInstitute', 'series', 'number', 'code', 'dateTimeField', 'place',
            'number_of_statement', 'amount', 'name_institute', 'name', 'surname', 'patronymic', 'INN',
            'numberInsuranceCertificate', 'dateBirthday', 'disability_group', 'disability_group_text', 'phoneNumber',
            'fullStateSupport', 'textfield1', 'textfield2'
        )


class Course(ModelForm):
    class Meta:
        model = CourseGroup
        fields = ('course', 'group', 'nameHeadman', 'nameInstitute')


class DisabilityGroupForm(ModelForm):
    class Meta:
        model = DisabilityGroup
        fields = ['categories', 'documents']
