# Generated by Django 3.2.6 on 2021-08-25 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210825_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='password_code',
            new_name='passport_code',
        ),
    ]