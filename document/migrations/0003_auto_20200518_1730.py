# Generated by Django 3.0.5 on 2020-05-18 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20200424_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisabilityGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=500)),
                ('documents', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='coursegroup',
            name='Group',
        ),
        migrations.RemoveField(
            model_name='coursegroup',
            name='namePraepostor',
        ),
        migrations.AddField(
            model_name='coursegroup',
            name='group',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='coursegroup',
            name='nameHeadman',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='coursegroup',
            name='course',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='coursegroup',
            name='nameInstitute',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='dateTimeField',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='number',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='place',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='series',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='FormOfEducation',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='INN',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='addressOfResidence',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='dateBirthday',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='disability',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='fullStateSupport',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='inProfCom',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='numberInsuranceCertificate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='numberTravelCard',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='pFact',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='passport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.Passport'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='patronymic',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='phoneNumber',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='preferentialCategory',
            field=models.CharField(max_length=1),
        ),
        migrations.CreateModel(
            name='Statement1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=1)),
                ('group', models.CharField(max_length=10)),
                ('nameHeadman', models.CharField(max_length=30)),
                ('nameInstitute', models.CharField(max_length=30)),
                ('series', models.CharField(blank=True, max_length=4, null=True)),
                ('number', models.CharField(blank=True, max_length=6, null=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('dateTimeField', models.CharField(blank=True, max_length=20, null=True)),
                ('place', models.CharField(blank=True, max_length=150, null=True)),
                ('number_of_statement', models.CharField(max_length=1)),
                ('amount', models.CharField(max_length=10)),
                ('name_institute', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('INN', models.CharField(max_length=10)),
                ('numberInsuranceCertificate', models.CharField(max_length=11)),
                ('dateBirthday', models.DateField()),
                ('disability_group_text', models.CharField(blank=True, default='Заполнить по необходимости', max_length=50, null=True)),
                ('phoneNumber', models.CharField(max_length=11)),
                ('fullStateSupport', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default=None, max_length=3)),
                ('textfield1', models.TextField()),
                ('textfield2', models.TextField()),
                ('disability_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.DisabilityGroup')),
            ],
        ),
    ]