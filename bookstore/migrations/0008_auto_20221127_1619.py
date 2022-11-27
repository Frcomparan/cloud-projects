# Generated by Django 3.2.3 on 2022-11-27 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_auto_20221127_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='end_time',
            field=models.DateField(default=datetime.datetime(2022, 12, 2, 16, 19, 59, 230265, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='start_time',
            field=models.DateField(default=datetime.datetime(2022, 11, 27, 16, 19, 59, 230245, tzinfo=utc)),
        ),
    ]