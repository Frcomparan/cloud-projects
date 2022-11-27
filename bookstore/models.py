from django.db import models
from django.conf import settings
from datetime import datetime, date, timedelta


# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=50, blank=False, null=False)
  description = models.CharField(max_length=256, blank=False, null=False)
  author = models.CharField(max_length=50, blank=False, null=False)
  release_date = models.DateField()
  pages = models.IntegerField()

class Borrow(models.Model):
  start_time = models.DateField(default=(date.today()))
  end_time = models.DateField(default=(date.today() + timedelta(days=5)))
  book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
  is_returned = models.BooleanField()