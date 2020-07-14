# Generated by Django 3.0.4 on 2020-05-24 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document', '0005_auto_20200520_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegroup',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='passport',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='course_Group',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.CourseGroup'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='passport',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.Passport'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='statement1',
            name='fullStateSupport',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Да', max_length=3),
        ),
    ]
