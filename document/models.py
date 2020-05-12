from django.db import models
from django.contrib.auth.models import User


class Passport(models.Model):
    series = models.IntegerField(name="Серия")
    number = models.IntegerField()
    code = models.IntegerField()
    dateTimeField = models.TextField()
    place = models.TextField()


class CourseGroup(models.Model):
    course = models.TextField()  # Курс
    Group = models.TextField()  # Группа
    namePraepostor = models.TextField()  # Имя старосты
    nameInstitute = models.TextField()


class SiteUser(models.Model):
    user = models.ForeignKey(User, name='user', on_delete=models.CASCADE)
    passport = models.ForeignKey(Passport, name='passport', on_delete=models.CASCADE)
    course_Group = models.ForeignKey(CourseGroup, name='course_Group', on_delete=models.CASCADE, blank=True, null=True)
    INN = models.IntegerField()
    pFact = models.TextField()
    dateBirthday = models.IntegerField()
    phoneNumber = models.IntegerField()
    patronymic = models.CharField(max_length=20)  # Отчество
    numberInsuranceCertificate = models.IntegerField()  # Страховое свидетельство
    disability = models.CharField(max_length=20)   # Инвалидность
    _STATUS_CHOICES = [  # Полное гос. обеспечение
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    ]
    fullStateSupport = models.CharField(max_length=3, choices=_STATUS_CHOICES)   # Полное гос. обеспечение
    preferentialCategory = models.CharField(max_length=1)  # Льготная категория
    numberTravelCard = models.IntegerField()  # Номер проездной карты
    addressOfResidence = models.TextField()  # Адрес фактического проживания
    FormOfEducation = models.CharField(max_length=1)  # Форма обучения
    inProfCom = models.CharField(max_length=3, choices=_STATUS_CHOICES)  # Состоит в профкоме или нет


class Statement1(models.Model):
    phoneNumber = models.IntegerField()
    patronymic = models.CharField(max_length=20)  # Отчество
    numberInsuranceCertificate = models.IntegerField()  # Страховое свидетельство
