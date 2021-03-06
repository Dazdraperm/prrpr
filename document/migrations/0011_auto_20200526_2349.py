# Generated by Django 3.0.4 on 2020-05-26 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0010_auto_20200526_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatementProfCom1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, max_length=10, null=True)),
                ('name_institute', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('surname', models.CharField(blank=True, max_length=15, null=True)),
                ('patronymic', models.CharField(blank=True, max_length=15, null=True)),
                ('apartment', models.CharField(blank=True, max_length=7, null=True)),
                ('house', models.CharField(blank=True, max_length=7, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('series', models.CharField(blank=True, max_length=4, null=True)),
                ('number', models.CharField(blank=True, max_length=6, null=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('dateTimeField', models.DateField(blank=True, max_length=20, null=True)),
                ('placeOfRegistration', models.CharField(blank=True, max_length=150, null=True)),
                ('dateBirthday', models.DateField(blank=True, max_length=8, null=True)),
                ('INN', models.CharField(blank=True, max_length=10, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('textfield1', models.CharField(blank=True, max_length=175, null=True)),
                ('textfield2', models.CharField(blank=True, max_length=175, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='statement1',
            name='amount',
        ),
        migrations.AddField(
            model_name='siteuser',
            name='name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='surname',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='apartment',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='house',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='index',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='apartment',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='house',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='index',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='patronymic',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='surname',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='textfield1',
            field=models.CharField(blank=True, max_length=175, null=True),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='textfield2',
            field=models.CharField(blank=True, max_length=175, null=True),
        ),
    ]
