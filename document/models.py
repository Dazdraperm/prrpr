from django.db import models
from django.contrib.auth.models import User

_STATUS_CHOICES = [
    ('Да', 'Да'),
    ('Нет', 'Нет'),
]


class Passport(models.Model):
    series = models.CharField(max_length=4, blank=True, null=True)
    number = models.CharField(max_length=6, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    dateTimeField = models.CharField(max_length=20, blank=True, null=True)
    place = models.CharField(max_length=150, blank=True, null=True)


class CourseGroup(models.Model):
    course = models.CharField(max_length=1, blank=True, null=True)  # Курс
    group = models.CharField(max_length=10, blank=True, null=True)  # Группа
    nameHeadman = models.CharField(max_length=30, blank=True, null=True)  # Имя старосты
    nameInstitute = models.CharField(max_length=30, blank=True, null=True)  # Название института



class SiteUser(models.Model):
    user = models.ForeignKey(User, name='user', on_delete=models.CASCADE)
    passport = models.ForeignKey(Passport, name='passport', on_delete=models.CASCADE, blank=True, null=True)
    course_Group = models.ForeignKey(CourseGroup, name='course_Group', on_delete=models.CASCADE, blank=True, null=True)
    INN = models.CharField(max_length=10)
    pFact = models.CharField(max_length=150)
    dateBirthday = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=11)
    patronymic = models.CharField(max_length=30)  # Отчество
    numberInsuranceCertificate = models.CharField(max_length=20)  # Страховое свидетельство
    disability = models.CharField(max_length=20)  # Инвалидность
    fullStateSupport = models.CharField(max_length=10, choices=_STATUS_CHOICES, blank=True,
                                        null=True)  # Полное гос. обеспечение
    preferentialCategory = models.CharField(max_length=1)  # Льготная категория
    numberTravelCard = models.CharField(max_length=20)  # Номер проездной карты
    addressOfResidence = models.CharField(max_length=20)  # Адрес фактического проживания
    FormOfEducation = models.CharField(max_length=1)  # Форма обучения
    inProfCom = models.CharField(max_length=10, choices=_STATUS_CHOICES, blank=True,
                                 null=True)  # Состоит в профкоме или нет


class DisabilityGroup(models.Model):
    categories = models.TextField(max_length=500)  # Категория
    documents = models.TextField(max_length=500)  # Подтверждающие документы

    def __str__(self):
        return '%s %s' % (self.categories, self.documents)


class Statement1(models.Model):
    course = models.CharField(max_length=1)  # Курс
    group = models.CharField(max_length=10)  # Группа
    nameHeadman = models.CharField(max_length=30)  # Имя старосты
    nameInstitute = models.CharField(max_length=30)  # Название института
    series = models.CharField(max_length=4, blank=True, null=True)
    number = models.CharField(max_length=6, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    dateTimeField = models.CharField(max_length=20, blank=True, null=True)
    place = models.CharField(max_length=150, blank=True, null=True)
    number_of_statement = models.CharField(max_length=1)
    amount = models.CharField(max_length=10)
    name_institute = models.CharField(max_length=20)  # Название института
    name = models.CharField(max_length=20)  # Имя
    surname = models.CharField(max_length=20)  # Фамилия
    patronymic = models.CharField(max_length=20)  # Отчество
    INN = models.CharField(max_length=10)  # ИНН
    numberInsuranceCertificate = models.CharField(max_length=11)  # Страховое свидетельство
    dateBirthday = models.DateField()  # День рождения
    disability_group = models.ForeignKey(DisabilityGroup, name='disability_group',
                                         on_delete=models.CASCADE)  # группа инвалидности
    disability_group_text = models.CharField(max_length=50, default='Заполнить по необходимости', blank=True,
                                             null=True)  # инвалидность по...
    phoneNumber = models.CharField(max_length=11)  # Номер телефона
    fullStateSupport = models.CharField(max_length=3, choices=_STATUS_CHOICES, default=None)  # Полное гос. обеспечение
    textfield1 = models.CharField(max_length=150)  # Просьба
    textfield2 = models.CharField(max_length=150)  # Приложение
