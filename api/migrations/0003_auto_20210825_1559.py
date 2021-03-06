# Generated by Django 3.2.6 on 2021-08-25 10:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usermodel_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('quantities', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('duedate', models.DateField(blank=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.category')),
            ],
        ),
        migrations.AddField(
            model_name='usermodel',
            name='password_code',
            field=models.CharField(blank=True, max_length=9, null=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9)]),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'user'), (2, 'vendor'), (3, 'accountant'), (4, 'product-manager'), (5, 'admin')], default=1),
        ),
        migrations.CreateModel(
            name='ProductItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantities', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sub_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('sub_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('status', models.BooleanField(default=False)),
                ('orderTime', models.TimeField(auto_now_add=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(to='api.ProductItems')),
            ],
        ),
    ]
