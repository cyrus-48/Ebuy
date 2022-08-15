from django.db import models


# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pimage = models.ImageField(default='default.png', blank=False, upload_to='uploads/')
    description = models.TextField(default="product")
    category = models.CharField(max_length=255 , default="phone")
    cost = models.CharField(max_length=50)
class Cart(models.Model):
    id = models.AutoField(primary_key =True)
    name = models.CharField(max_length=255)
    pimage = models.ImageField(default='default.png', blank=False, upload_to='cart/')
    cost = models.CharField(max_length=255)