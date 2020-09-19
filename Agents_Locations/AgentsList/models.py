from django.db import models

# Create your models here.
class Agents_Details(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length= 50)
    state = models.CharField(max_length=30)