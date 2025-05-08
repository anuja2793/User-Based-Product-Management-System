from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=700)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    offer=models.CharField(max_length=100)