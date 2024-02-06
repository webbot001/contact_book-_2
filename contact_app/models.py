from django.db import models

# Create your models here.
class user_data(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class contacts(models.Model):
    added_by = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    gender   = models.CharField(max_length=100)

class contacts_data(models.Model):
    added_by = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    gender   = models.CharField(max_length=100)