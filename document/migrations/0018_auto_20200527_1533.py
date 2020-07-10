# Generated by Django 3.0.4 on 2020-05-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0017_auto_20200527_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='dateBirthday',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='date_day',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='День выдачи Паспорта'),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='dateBirthday',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Страховое свидетельство'),
        ),
        migrations.AlterField(
            model_name='statementprofcom1',
            name='dateBirthday',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Дата рождения'),
        ),
    ]