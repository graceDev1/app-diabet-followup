from django.db import models

class User(models.Model):
    fullName = models.CharField(max_length=255)
    weight = models.FloatField()
    height = models.FloatField()
    birthday = models.DateField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

