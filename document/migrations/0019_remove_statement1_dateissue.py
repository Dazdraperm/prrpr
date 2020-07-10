from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0018_auto_20200527_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement1',
            name='dateIssue',
        ),
    ]
