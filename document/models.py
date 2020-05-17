from django.db import models
from django.contrib.auth.models import User


class Passport(models.Model):
    series = models.CharField(max_length=4, blank=True, null=True)
    number = models.CharField(max_length=6, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    dateTimeField = models.CharField(max_length=20, blank=True, null=True)
    place = models.CharField(max_length=150, blank=True, null=True)


class CourseGroup(models.Model):
    course = models.CharField(max_length=1)  # Курс
    group = models.CharField(max_length=10, default='1')  # Группа
    nameHeadman = models.CharField(max_length=30)  # Имя старосты
    nameInstitute = models.CharField(max_length=30)     # Название института


class SiteUser(models.Model):
    user = models.ForeignKey(User, name='user', on_delete=models.CASCADE)
    passport = models.ForeignKey(Passport, name='passport', on_delete=models.CASCADE)
    course_Group = models.ForeignKey(CourseGroup, name='course_Group', on_delete=models.CASCADE, null=True, blank=True)
    INN = models.CharField(max_length=10)
    pFact = models.CharField(max_length=20)
    dateBirthday = models.IntegerField()
    phoneNumber = models.IntegerField()
    patronymic = models.CharField(max_length=30)  # Отчество
    numberInsuranceCertificate = models.IntegerField()  # Страховое свидетельство
    disability = models.CharField(max_length=20)   # Инвалидность
    _STATUS_CHOICES = [  # Полное гос. обеспечение
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    ]
    fullStateSupport = models.CharField(max_length=3, choices=_STATUS_CHOICES)   # Полное гос. обеспечение
    preferentialCategory = models.CharField(max_length=1)  # Льготная категория
    numberTravelCard = models.IntegerField()  # Номер проездной карты
    addressOfResidence = models.CharField(max_length=20)  # Адрес фактического проживания
    FormOfEducation = models.CharField(max_length=1)  # Форма обучения
    inProfCom = models.CharField(max_length=3, choices=_STATUS_CHOICES)  # Состоит в профкоме или нет


class Statement1(models.Model):
    course_Group = models.ForeignKey(CourseGroup, name='course_Group', on_delete=models.CASCADE)
    nameInstitute = models.CharField(max_length=20)      # Название института
    name = models.CharField(max_length=20)   # Имя
    surname = models.CharField(max_length=20)    # Фамилия
    patronymic = models.CharField(max_length=20)     # Отчество
    phoneNumber = models.IntegerField()     # Номер телефона
    numberInsuranceCertificate = models.IntegerField()  # Страховое свидетельство
