# Generated by Django 3.0.4 on 2020-04-23 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.TextField()),
                ('Group', models.TextField()),
                ('namePraepostor', models.TextField()),
                ('nameInstitute', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='siteuser',
            name='courseAndGroup',
        ),
        migrations.RemoveField(
            model_name='siteuser',
            name='nameInstitute',
        ),
        migrations.RemoveField(
            model_name='siteuser',
            name='namePraepostor',
        ),
        migrations.AddField(
            model_name='siteuser',
            name='course_Group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.CourseGroup'),
        ),
    ]
