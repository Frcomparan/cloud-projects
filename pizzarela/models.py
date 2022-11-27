from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  description = models.CharField(max_length=256, blank=False, null=False)

class Product(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  price = models.DecimalField(max_digits=8, decimal_places=3, null=False, validators=[MinValueValidator(0)])
  stock = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
  category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Order(models.Model):
  created_at = models.DateField(default=now(), null=False)
  total = models.DecimalField(max_digits=10, decimal_places=3, default=0, validators=[MinValueValidator(0)])

class OrderItem(models.Model):
  quantity = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
  product = models.ForeignKey('Product', on_delete=models.CASCADE)
  order = models.ForeignKey('Order', on_delete=models.CASCADE)

