# Generated by Django 3.2.3 on 2022-11-27 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20221127_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='end_time',
            field=models.DateField(default=datetime.datetime(2022, 12, 2, 15, 30, 19, 134652, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='start_time',
            field=models.DateField(default=datetime.datetime(2022, 11, 27, 15, 30, 19, 134632, tzinfo=utc)),
        ),
    ]
