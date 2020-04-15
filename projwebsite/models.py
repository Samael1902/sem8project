from django.db import models

# Create your models here.

class UsersFR(models.Model):

    fname: models.CharField(max_length=100)
    lname: models.CharField(max_length=100)
    nname: models.CharField(max_length=100)
    email: models.EmailField()
    passwd1: models.CharField(max_length=100)
    passwd2: models.CharField(max_length=100)