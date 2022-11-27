# Generated by Django 3.2.3 on 2022-11-27 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzarela', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=8, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]