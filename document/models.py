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
    series = models.CharField(max_length=4, blank=True, null=True, verbose_name='Серия')
    number = models.CharField(max_length=6, blank=True, null=True, verbose_name='Номер')
    place = models.CharField(max_length=100, blank=True, null=True, verbose_name='Кем выдан')
    code = models.CharField(max_length=7, blank=True, null=True, verbose_name='Код подразделения')
    date_day = models.CharField(max_length=2, blank=True, null=True, verbose_name='День выдачи Паспорта')  # День выдачи
    date_month = models.CharField(max_length=8, blank=True, null=True, verbose_name='Месяц выдачи Паспорта')  # Месяц выдачи
    date_year = models.IntegerField(max_length=2, blank=True, null=True, verbose_name='Год выдачи Паспорта')  # Год выдачи
    placeOfRegistration = models.CharField(max_length=150, blank=True, null=True, verbose_name='Место регистрации')  # Место регистрации
    dateBirthday = models.CharField(max_length=8, blank=True, null=True, verbose_name='День рождения')


class CourseGroup(models.Model):
    user = models.OneToOneField(User, name='user', on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=1, blank=True, null=True, verbose_name='Курс')  # Курс
    group = models.CharField(max_length=10, blank=True, null=True, verbose_name='Группа')  # Группа
    nameHeadman = models.CharField(max_length=30, blank=True, null=True, verbose_name='ФИО старосты')  # Имя старосты
    nameInstitute = models.CharField(max_length=30, blank=True, null=True, verbose_name='Название института')  # Название института


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
    name = models.CharField(max_length=15, blank=True, null=True, verbose_name='Имя')
    surname = models.CharField(max_length=15, blank=True, null=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, blank=True, null=True, verbose_name='Отчество')  # Отчество
    INN = models.CharField(max_length=10, blank=True, null=True, verbose_name='ИНН')
    street = models.CharField(max_length=150, blank=True, null=True, verbose_name='Улица')  # Место жительства
    apartment = models.CharField(max_length=7, blank=True, null=True, verbose_name='Квартира')  # Квартира
    index = models.CharField(max_length=8, blank=True, null=True, verbose_name='Индекс')  # Почтовый индекс
    house = models.CharField(max_length=7, blank=True, null=True, verbose_name='Номер Дома')  # Дом
    phoneNumber = models.CharField(max_length=11, blank=True, null=True, verbose_name='Сотовый Телефон')

    numberInsuranceCertificate = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер '
                                                                                                     'страхового '
                                                                                                     'свидетельства')
    # Страховое свидетельство
    disability = models.CharField(max_length=20, blank=True, null=True, verbose_name='Группа инвалидности')  # Инвалидность
    fullStateSupport = models.CharField(max_length=10, choices=_STATUS_CHOICES, blank=True,
                                        null=True, verbose_name='Есть ли полное гос. обеспечение')  # Полное гос. обеспечение
    numberTravelCard = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер проездной карты')  # Номер проездной карты
    FormOfEducation = models.CharField(max_length=1, blank=True, null=True, verbose_name='Форма Обучения')  # Форма обучения
    inProfCom = models.CharField(max_length=10, choices=_STATUS_CHOICES, blank=True,
                                 null=True, verbose_name='Состоите ли вы в профкоме')  # Состоит в профкоме или нет


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
    course = models.CharField(max_length=1, blank=True, null=True, verbose_name='Курс')  # Курс
    group = models.CharField(max_length=10, blank=True, null=True, verbose_name='Группа')  # Группа
    nameHeadman = models.CharField(max_length=30, blank=True, null=True, verbose_name='фИО старосты')  # Имя старосты
    series = models.CharField(max_length=4, blank=True, null=True, verbose_name='Серия')  # Серия
    number = models.CharField(max_length=6, blank=True, null=True, verbose_name='Номер')  # Номер
    code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Код подразделения')  # Код подразделения
    date_day = models.IntegerField(max_length=2, blank=True, null=True, verbose_name='День выдачи Паспорта')  # День выдачи
    date_month = models.CharField(max_length=8, blank=True, null=True, verbose_name='Месяц выдачи Паспорта')  # Месяц выдачи
    date_year = models.IntegerField(max_length=2, blank=True, null=True, verbose_name='Год выдачи Паспорта')  # Год выдачи
    place = models.CharField(max_length=100, blank=True, null=True, verbose_name='Паспорт выдан')  # Паспорт выдан
    index = models.IntegerField(max_length=8, blank=True, null=True, verbose_name='Индекс')  # Почтовый индекс
    house = models.IntegerField(max_length=7, blank=True, null=True, verbose_name='Дом')  # Дом
    street = models.CharField(max_length=15, blank=True, null=True, verbose_name='Улица')  # Улица
    apartment = models.IntegerField(max_length=7, blank=True, null=True, verbose_name='Квартира')  # Квартира
    number_of_statement = models.CharField(max_length=1, blank=True, null=True, verbose_name='Номер заявления')  # Номер заявления
    # amount = models.CharField(max_length=10, blank=True, null=True)  # Сумма денег
    name_institute = models.CharField(max_length=20, blank=True, null=True, verbose_name='Название института')  # Название института
    name = models.CharField(max_length=15, blank=True, null=True, verbose_name='Имя')  # Имя
    surname = models.CharField(max_length=15, blank=True, null=True, verbose_name='Фамилия')  # Фамилия
    patronymic = models.CharField(max_length=15, blank=True, null=True, verbose_name='Отчество')  # Отчество
    INN = models.CharField(max_length=10, blank=True, null=True, verbose_name='ИНН')  # ИНН
    numberInsuranceCertificate = models.CharField(max_length=11, blank=True, null=True, verbose_name='Страховое свидетельство')  # Страховое свидетельство
    dateBirthday = models.CharField(max_length=8, blank=True, null=True, verbose_name='День рождения')  # День рождения
    disability_group = models.CharField(max_length=20, blank=True, null=True, verbose_name='Группа инвалидности')  # группа инвалидности
    phoneNumber = models.CharField(max_length=11, blank=True, null=True, verbose_name='Номер телефона')  # Номер телефона
    fullStateSupport = models.CharField(max_length=3, choices=_STATUS_CHOICES, default=None, blank=True,
                                        null=True, verbose_name='Полное гос.обеспечение')  # Полное гос. обеспечение
    textfield1 = models.CharField(max_length=175, blank=True, null=True, verbose_name='Просьба')  # Просьба
    textfield2 = models.CharField(max_length=175, blank=True, null=True, verbose_name='Приложение')  # Приложение


class StatementProfCom1(models.Model):
    group = models.CharField(max_length=10, blank=True, null=True, verbose_name='Группа')  # Группа
    name_institute = models.CharField(max_length=20, blank=True, null=True, verbose_name='Название института')  # Название института
    name = models.CharField(max_length=15, blank=True, null=True, verbose_name='Имя')  # Имя
    surname = models.CharField(max_length=15, blank=True, null=True, verbose_name='Фамилия')  # Фамилия
    patronymic = models.CharField(max_length=15, blank=True, null=True, verbose_name='Отчество')  # Отчество
    apartment = models.CharField(max_length=7, blank=True, null=True, verbose_name='Квартира')  # Квартира
    house = models.CharField(max_length=7, blank=True, null=True, verbose_name='Дом')  # Дом
    street = models.CharField(max_length=100, blank=True, null=True, verbose_name='Улица')
    place = models.CharField(max_length=100, blank=True, null=True, verbose_name='Паспорт выдан')
    series = models.CharField(max_length=4, blank=True, null=True, verbose_name='Серия')
    number = models.CharField(max_length=6, blank=True, null=True, verbose_name='Номер')
    date_day = models.IntegerField(max_length=2, blank=True, null=True, verbose_name='День выдачи Паспорта')  # День выдачи
    date_month = models.CharField(max_length=8, blank=True, null=True, verbose_name='Месяц выдачи Паспорта')  # Месяц выдачи
    date_year = models.IntegerField(max_length=2, blank=True, null=True, verbose_name='День выдачи Паспорта')  # Год выдачи
    dateBirthday = models.CharField(max_length=8, blank=True, null=True, verbose_name='Дата рождения')
    INN = models.CharField(max_length=10, blank=True, null=True, verbose_name='ИНН')  # ИНН
    phoneNumber = models.CharField(max_length=11, blank=True, null=True, verbose_name='Номер телефона')  # Номер телефона
    textfield1 = models.CharField(max_length=175, blank=True, null=True, verbose_name='Просьба')  # Просьба
    textfield2 = models.CharField(max_length=175, blank=True, null=True, verbose_name='Приложение')  # Приложение
