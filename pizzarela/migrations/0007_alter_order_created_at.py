# Generated by Django 3.2.3 on 2022-11-28 17:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pizzarela', '0006_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 11, 28, 17, 10, 55, 645037, tzinfo=utc)),
        ),
    ]