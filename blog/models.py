from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    job = models.CharField(max_length=250)
    salary = models.BigIntegerField(null=True)