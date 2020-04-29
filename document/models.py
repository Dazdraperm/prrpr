from django.db import models
from django.contrib.auth.models import User


class Passport(models.Model):
    series = models.IntegerField()
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
    dateBirthday = models.TextField()
    phoneNumber = models.IntegerField()
    patronymic = models.TextField()  # Отчество
    numberInsuranceCertificate = models.TextField()  # Страховое свидетельство
    disability = models.TextField()  # Инвалидность
    fullStateSupport = models.TextField()  # Полное гос. обеспечение
    preferentialCategory = models.TextField()  # Льготная категория
    numberTravelCard = models.IntegerField()  # Номер проездной карты
    addressOfResidence = models.TextField()  # Адрес фактического проживания
    FormOfEducation = models.TextField()  # Форма обучения
    inProfCom = models.TextField()  # Состоит в профкоме или нет
