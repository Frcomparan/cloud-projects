# Generated by Django 3.2.3 on 2022-11-27 22:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pizzarela', '0004_auto_20221127_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 11, 27, 22, 20, 7, 931582, tzinfo=utc)),
        ),
    ]
