# Generated by Django 3.2.3 on 2022-11-27 02:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_alter_borrow_is_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='end_time',
            field=models.DateField(default=datetime.datetime(2022, 12, 2, 2, 36, 57, 270704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='start_time',
            field=models.DateField(default=datetime.datetime(2022, 11, 27, 2, 36, 57, 270684, tzinfo=utc)),
        ),
    ]