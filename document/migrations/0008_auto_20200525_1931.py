# Generated by Django 3.0.6 on 2020-05-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0007_auto_20200524_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='series',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='FormOfEducation',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='INN',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='addressOfResidence',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='disability',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='numberInsuranceCertificate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='numberTravelCard',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='preferentialCategory',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='INN',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='amount',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='course',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='dateBirthday',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='disability_group',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='fullStateSupport',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Да', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='group',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='nameHeadman',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='name_institute',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='numberInsuranceCertificate',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='number_of_statement',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='surname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='textfield1',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='textfield2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
