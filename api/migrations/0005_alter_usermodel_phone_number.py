# Generated by Django 3.2.6 on 2021-08-25 14:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_password_code_usermodel_passport_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]