from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class wards(models.Model):

    wardno = models.CharField(max_length = 200, primary_key=True)
    wardname = models.CharField(max_length = 200)


class houseowner(AbstractUser):
    username  =None
    
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200, unique=True)
    phoneno = models.CharField(max_length = 200, unique=True)
    address = models.CharField(max_length = 1000)
    pincode = models.CharField(max_length = 50)
    wardno = models.ForeignKey(wards, on_delete=models.CASCADE)
    password = models.CharField(max_length = 200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
