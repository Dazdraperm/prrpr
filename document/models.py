from django.db import models
from django.contrib.auth.models import User


class Passport(models.Model):
    series = models.IntegerField()
    number = models.IntegerField()
    code = models.IntegerField()
    dateTimeField = models.TextField()
    place = models.TextField()


class SiteUser(models.Model):
    user = models.ForeignKey(User, name='user', on_delete=models.CASCADE)
    passport = models.ForeignKey(Passport, name='passport', on_delete=models.CASCADE)
    INN = models.IntegerField()
    pFact = models.TextField()
    dateBirthday = models.TextField()
    phoneNumber = models.IntegerField()
    courseAndGroup = models.TextField()  # Курс-группа
    patronymic = models.TextField()  # Отчество
    numberInsuranceCertificate = models.TextField()  # Страховое свидетельство
    disability = models.TextField()
    fullStateSupport = models.TextField()  # Полное гос. обеспечение
    preferentialCategory = models.TextField()  # Льготная категория
    nameInstitute = models.TextField()
    namePraepostor = models.TextField()  # Имя старосты
    numberTravelCard = models.IntegerField()  # Номер проездной карты
    addressOfResidence = models.TextField()  # Адрес фактического проживания
    FormOfEducation = models.TextField()  # Форма обучения
    inProfCom = models.TextField()  # Состоит в профкоме или нет

