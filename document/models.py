from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

_STATUS_CHOICES = [
    ('Да', 'Да'),
    ('Нет', 'Нет'),
]

CHOICES_STATEMENT = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
]


class Passport(models.Model):
    user = models.OneToOneField(User, name='user', on_delete=models.CASCADE, blank=True, null=True)
    series = models.CharField(max_length=4, blank=True, null=True, verbose_name='Серия')
    number_passport = models.CharField(max_length=6, blank=True, null=True, verbose_name='Номер паспорта')
    issued_passport = models.CharField(max_length=100, blank=True, null=True, verbose_name='Кем выдан')
    unit_code = models.CharField(max_length=7, blank=True, null=True, verbose_name='Код подразделения')
    passport_issue_day = models.CharField(max_length=2, blank=True, null=True,
                                          verbose_name='День выдачи Паспорта')  # День выдачи
    passport_issue_month = models.CharField(max_length=8, blank=True, null=True,
                                            verbose_name='Месяц выдачи Паспорта')  # Месяц выдачи
    passport_issue_year = models.CharField(max_length=2, blank=True, null=True,
                                           verbose_name='Год выдачи Паспорта')  # Год выдачи
    place_registration = models.CharField(max_length=150, blank=True, null=True,
                                          verbose_name='Место регистрации')  # Место регистрации
    date_birthday = models.CharField(max_length=8, blank=True, null=True, verbose_name='День рождения')


class CourseGroup(models.Model):
    user = models.OneToOneField(User, name='user', on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=1, blank=True, null=True, verbose_name='Курс')  # Курс
    group = models.CharField(max_length=10, blank=True, null=True, verbose_name='Группа')  # Группа
    FIO_headman = models.CharField(max_length=30, blank=True, null=True, verbose_name='ФИО старосты')  # Имя старосты
    name_institute = models.CharField(max_length=30, blank=True, null=True,
                                      verbose_name='Название института')  # Название института


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
    location_street = models.CharField(max_length=150, blank=True, null=True, verbose_name='Улица')  # Место жительства
    location_apartment = models.CharField(max_length=7, blank=True, null=True, verbose_name='Квартира')  # Квартира
    location_house = models.CharField(max_length=7, blank=True, null=True, verbose_name='Номер Дома')  # Дом
    post_code = models.CharField(max_length=8, blank=True, null=True, verbose_name='Индекс')  # Почтовый индекс
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='Сотовый Телефон')
    number_insurance_certificate = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер '
                                                                                                       'страхового '
                                                                                                       'свидетельства')
    disability_group = models.CharField(max_length=20, blank=True, null=True,
                                        verbose_name='Группа инвалидности')  # Инвалидность
    full_state_support = models.CharField(max_length=10, choices=_STATUS_CHOICES, blank=True,
                                          null=True,
                                          verbose_name='Есть ли полное гос. обеспечение')  # Полное гос. обеспечение
    number_travel_card = models.CharField(max_length=20, blank=True, null=True,
                                          verbose_name='Номер проездной карты')  # Номер проездной карты
    form_education = models.CharField(max_length=1, blank=True, null=True,
                                      verbose_name='Форма Обучения')  # Форма обучения
    state_prof_com = models.CharField(max_length=10, choices=_STATUS_CHOICES, blank=True,
                                      null=True, verbose_name='Состоите ли вы в профкоме')  # Состоит в профкоме или нет


@receiver(post_save, sender=User)
def new_user(sender, instance, created, **kwargs):
    if created:
        SiteUser.objects.create(user=instance)
        instance.siteuser.save()


class DisabilityGroup(models.Model):
    categories = models.TextField(max_length=500)  # Категория
    supporting_documents = models.TextField(max_length=500)  # Подтверждающие документы

    def __str__(self):
        return '%s %s' % (self.categories, self.supporting_documents)


class Statement1(models.Model):
    # Курс
    course = models.CharField(max_length=1, blank=True, null=True, verbose_name='Курс')  # Курс
    group = models.CharField(max_length=10, blank=True, null=True, verbose_name='Группа')  # Группа
    FIO_headman = models.CharField(max_length=30, blank=True, null=True, verbose_name='ФИО старосты')  # Имя старосты
    name_institute = models.CharField(max_length=30, blank=True, null=True,
                                      verbose_name='Название института')  # Название института

    # Пасспорт
    series = models.CharField(max_length=4, blank=True, null=True, verbose_name='Серия')  # Серия
    number_passport = models.CharField(max_length=6, blank=True, null=True, verbose_name='Номер паспорта')
    issued_passport = models.CharField(max_length=100, blank=True, null=True, verbose_name='Кем выдан')
    unit_code = models.CharField(max_length=7, blank=True, null=True, verbose_name='Код подразделения')
    passport_issue_day = models.CharField(max_length=2, blank=True, null=True,
                                          verbose_name='День выдачи Паспорта')  # День выдачи
    passport_issue_month = models.CharField(max_length=8, blank=True, null=True,
                                            verbose_name='Месяц выдачи Паспорта')  # Месяц выдачи
    passport_issue_year = models.CharField(max_length=2, blank=True, null=True,
                                           verbose_name='Год выдачи Паспорта')  # Год выдачи
    date_birthday = models.CharField(max_length=8, blank=True, null=True, verbose_name='День рождения')

    # Основные
    post_code = models.CharField(max_length=8, blank=True, null=True, verbose_name='Индекс')  # Почтовый индекс
    location_street = models.CharField(max_length=150, blank=True, null=True, verbose_name='Улица')  # Место жительства
    location_apartment = models.CharField(max_length=7, blank=True, null=True, verbose_name='Квартира')  # Квартира
    location_house = models.CharField(max_length=7, blank=True, null=True, verbose_name='Номер Дома')  # Дом
    number_of_statement = models.CharField(max_length=1, choices=CHOICES_STATEMENT, default=None, blank=True, null=True,
                                           verbose_name='Номер заявления')  # Номер заявления
    name = models.CharField(max_length=15, blank=True, null=True, verbose_name='Имя')  # Имя
    surname = models.CharField(max_length=15, blank=True, null=True, verbose_name='Фамилия')  # Фамилия
    patronymic = models.CharField(max_length=15, blank=True, null=True, verbose_name='Отчество')  # Отчество
    INN = models.CharField(max_length=10, blank=True, null=True, verbose_name='ИНН')  # ИНН
    number_insurance_certificate = models.CharField(max_length=11, blank=True, null=True,
                                                    verbose_name='Страховое свидетельство')  # Страховое свидетельство
    disability_group = models.CharField(max_length=20, blank=True, null=True,
                                        verbose_name='Группа инвалидности')  # группа инвалидности
    phone_number = models.CharField(max_length=11, blank=True, null=True,
                                    verbose_name='Номер телефона')  # Номер телефона
    full_state_support = models.CharField(max_length=3, choices=_STATUS_CHOICES, default=None, blank=True,
                                          null=True, verbose_name='Полное гос.обеспечение')  # Полное гос. обеспечение

    # Уникальные
    request = models.CharField(max_length=175, blank=True, null=True, verbose_name='Просьба')  # Просьба
    annex = models.CharField(max_length=175, blank=True, null=True, verbose_name='Приложение')  # Приложение


class StatementProfCom1(models.Model):
    # Курс
    group = models.CharField(max_length=10, blank=True, null=True, verbose_name='Группа')  # Группа
    name_institute = models.CharField(max_length=20, blank=True, null=True,
                                      verbose_name='Название института')  # Название института

    # Основные
    name = models.CharField(max_length=15, blank=True, null=True, verbose_name='Имя')  # Имя
    surname = models.CharField(max_length=15, blank=True, null=True, verbose_name='Фамилия')  # Фамилия
    patronymic = models.CharField(max_length=15, blank=True, null=True, verbose_name='Отчество')  # Отчество
    location_street = models.CharField(max_length=150, blank=True, null=True, verbose_name='Улица')  # Место жительства
    location_apartment = models.CharField(max_length=7, blank=True, null=True, verbose_name='Квартира')  # Квартира
    location_house = models.CharField(max_length=7, blank=True, null=True, verbose_name='Номер Дома')  # Дом
    INN = models.CharField(max_length=10, blank=True, null=True, verbose_name='ИНН')  # ИНН
    phone_number = models.CharField(max_length=11, blank=True, null=True,
                                    verbose_name='Номер телефона')  # Номер телефона

    # Пасспорт
    issued_passport = models.CharField(max_length=100, blank=True, null=True, verbose_name='Кем выдан')
    series = models.CharField(max_length=4, blank=True, null=True, verbose_name='Серия')
    number_passport = models.CharField(max_length=6, blank=True, null=True, verbose_name='Номер паспорта')
    passport_issue_day = models.CharField(max_length=2, blank=True, null=True,
                                          verbose_name='День выдачи Паспорта')  # День выдачи
    passport_issue_month = models.CharField(max_length=8, blank=True, null=True,
                                            verbose_name='Месяц выдачи Паспорта')  # Месяц выдачи
    passport_issue_year = models.CharField(max_length=2, blank=True, null=True,
                                           verbose_name='Год выдачи Паспорта')  # Год выдачи
    date_birthday = models.CharField(max_length=8, blank=True, null=True, verbose_name='День рождения')

    request = models.CharField(max_length=175, blank=True, null=True, verbose_name='Просьба')  # Просьба
    annex = models.CharField(max_length=175, blank=True, null=True, verbose_name='Приложение')  # Приложение
