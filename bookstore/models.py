from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=50, blank=False, null=False)
  description = models.CharField(max_length=256, blank=False, null=False)
  author = models.CharField(max_length=50, blank=False, null=False)
  release_date = models.DateField()
  pages = models.IntegerField()

class Borrow(models.Model):
  start_time = models.DateField(default=(now()), null=False)
  end_time = models.DateField(default=(now() + timedelta(days=5)), null=False)
  book_id = models.ForeignKey('Book', on_delete=models.CASCADE)
  is_returned = models.BooleanField(default=False)