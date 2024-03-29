# Generated by Django 3.2.3 on 2022-11-27 00:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('pages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField(default=datetime.date(2022, 11, 27))),
                ('end_time', models.DateField(default=datetime.date(2022, 12, 2))),
                ('is_returned', models.BooleanField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.book')),
            ],
        ),
    ]
