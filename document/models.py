from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

_STATUS_CHOICES = [
    ('Да', 'Да'),
    ('Нет', 'Нет'),
]


class Passport(models.Model):
    user = models.OneToOneField(User, name='user', on_delete=models.CASCADE, blank=True, null=True)
    series = models.CharField(max_length=4, blank=True, null=True)
    number = models.CharField(max_length=6, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    dateTimeField = models.DateField(max_length=20, blank=True, null=True)  #
    placeOfRegistration = models.CharField(max_length=150, blank=True, null=True)  # Место регистрации
    dateBirthday = models.DateField(max_length=8, blank=True, null=True)


class CourseGroup(models.Model):
    user = models.OneToOneField(User, name='user', on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=1, blank=True, null=True)  # Курс
    group = models.CharField(max_length=10, blank=True, null=True)  # Группа
    nameHeadman = models.CharField(max_length=30, blank=True, null=True)  # Имя старосты
    nameInstitute = models.CharField(max_length=30, blank=True, null=True)  # Название института


@receiver(post_save, sender=User)
def new_course_group(sender, instance, created, **kwargs):
    if created:
        CourseGroup.objects.create(user=instance)
        instance.coursegroup.save()


@receiver(post_save, sender=User)
def new_passport(sender, instance, created, **kwargs):
    if created:
        Passport.objects.create(user=instance)
        instance.passport.save()


class SiteUser(models.Model):
    user = models.OneToOneField(User, name='user', on_delete=models.CASCADE)
    passport = models.OneToOneField(Passport, name='passport', on_delete=models.CASCADE, blank=True, null=True)
    course_Group = models.OneToOneField(CourseGroup, name='course_Group', on_delete=models.CASCADE, blank=True,
                                        null=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    surname = models.CharField(max_length=15, blank=True, null=True)
    patronymic = models.CharField(max_length=30, blank=True, null=True)  # Отчество
    INN = models.CharField(max_length=10, blank=True, null=True)
    pFact = models.CharField(max_length=150, blank=True, null=True)  # Место жительства
    apartment = models.CharField(max_length=7, blank=True, null=True)  # Квартира
    index = models.CharField(max_length=8, blank=True, null=True)  # Почтовый индекс
    house = models.CharField(max_length=7, blank=True, null=True)  # Дом
    phoneNumber = models.CharField(max_length=11, blank=True, null=True)

    numberInsuranceCertificate = models.CharField(max_length=20, blank=True, null=True)  # Страховое свидетельство
    disability = models.CharField(max_length=20, blank=True, null=True)  # Инвалидность
    fullStateSupport = models.CharField(max_length=10, choices=_STATUS_CHOICES, blank=True,
                                        null=True)  # Полное гос. обеспечение
    preferentialCategory = models.CharField(max_length=1, blank=True, null=True)  # Льготная категория
    numberTravelCard = models.CharField(max_length=20, blank=True, null=True)  # Номер проездной карты
    addressOfResidence = models.CharField(max_length=20, blank=True, null=True)  # Адрес фактического проживания
    FormOfEducation = models.CharField(max_length=1, blank=True, null=True)  # Форма обучения
    inProfCom = models.CharField(max_length=10, choices=_STATUS_CHOICES, blank=True,
                                 null=True)  # Состоит в профкоме или нет


@receiver(post_save, sender=User)
def new_user(sender, instance, created, **kwargs):
    if created:
        SiteUser.objects.create(user=instance)
        instance.siteuser.save()


class DisabilityGroup(models.Model):
    categories = models.TextField(max_length=500)  # Категория
    documents = models.TextField(max_length=500)  # Подтверждающие документы

    def __str__(self):
        return '%s %s' % (self.categories, self.documents)


class Statement1(models.Model):
    course = models.CharField(max_length=1, blank=True, null=True)  # Курс
    group = models.CharField(max_length=10, blank=True, null=True)  # Группа
    nameHeadman = models.CharField(max_length=30, blank=True, null=True)  # Имя старосты
    series = models.CharField(max_length=4, blank=True, null=True, verbose_name='Серия')  # Серия
    number = models.CharField(max_length=6, blank=True, null=True)  # Номер
    code = models.CharField(max_length=20, blank=True, null=True)  # Код подразделения
    dateTimeField = models.DateField(max_length=20, blank=True, null=True)  # Дата выдачи паспорта
    date_day = models.IntegerField(max_length=2, blank=True, null=True)  # День выдачи
    date_month = models.CharField(max_length=8, blank=True, null=True)  # Месяц выдачи
    date_year = models.IntegerField(max_length=2, blank=True, null=True)  # Год выдачи
    place = models.CharField(max_length=100, blank=True, null=True)  # Паспорт выдан
    index = models.IntegerField(max_length=8, blank=True, null=True)  # Почтовый индекс
    house = models.IntegerField(max_length=7, blank=True, null=True)  # Дом
    street = models.CharField(max_length=15, blank=True, null=True)  # Улица
    apartment = models.IntegerField(max_length=7, blank=True, null=True)  # Квартира
    number_of_statement = models.CharField(max_length=1, blank=True, null=True)  # Номер заявления
    # amount = models.CharField(max_length=10, blank=True, null=True)  # Сумма денег
    name_institute = models.CharField(max_length=20, blank=True, null=True)  # Название института
    name = models.CharField(max_length=15, blank=True, null=True)  # Имя
    surname = models.CharField(max_length=15, blank=True, null=True)  # Фамилия
    patronymic = models.CharField(max_length=15, blank=True, null=True)  # Отчество
    INN = models.CharField(max_length=10, blank=True, null=True)  # ИНН
    numberInsuranceCertificate = models.CharField(max_length=11, blank=True, null=True)  # Страховое свидетельство
    dateBirthday = models.DateField(max_length=8, blank=True, null=True)  # День рождения
    disability_group = models.CharField(max_length=20, blank=True, null=True)  # группа инвалидности
    disability_group_text = models.CharField(max_length=50, blank=True, null=True)  # инвалидность по...
    phoneNumber = models.CharField(max_length=11, blank=True, null=True)  # Номер телефона
    fullStateSupport = models.CharField(max_length=3, choices=_STATUS_CHOICES, default='Да', blank=True,
                                        null=True)  # Полное гос. обеспечение
    textfield1 = models.CharField(max_length=175, blank=True, null=True)  # Просьба
    textfield2 = models.CharField(max_length=175, blank=True, null=True)  # Приложение


class StatementProfCom1(models.Model):
    group = models.CharField(max_length=10, blank=True, null=True)  # Группа
    name_institute = models.CharField(max_length=20, blank=True, null=True)  # Название института
    name = models.CharField(max_length=15, blank=True, null=True)  # Имя
    surname = models.CharField(max_length=15, blank=True, null=True)  # Фамилия
    patronymic = models.CharField(max_length=15, blank=True, null=True)  # Отчество
    apartment = models.CharField(max_length=7, blank=True, null=True)  # Квартира
    house = models.CharField(max_length=7, blank=True, null=True)  # Дом
    street = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    series = models.CharField(max_length=4, blank=True, null=True)
    number = models.CharField(max_length=6, blank=True, null=True)
    dateTimeField = models.DateField(max_length=20, blank=True, null=True)  #
    dateBirthday = models.DateField(max_length=8, blank=True, null=True)
    INN = models.CharField(max_length=10, blank=True, null=True)  # ИНН
    phoneNumber = models.CharField(max_length=11, blank=True, null=True)  # Номер телефона
    textfield1 = models.CharField(max_length=175, blank=True, null=True)  # Просьба
    textfield2 = models.CharField(max_length=175, blank=True, null=True)  # Приложение
