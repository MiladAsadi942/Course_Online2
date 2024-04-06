from django.db import models

from django_jalali.db import models as jmodels
from django.contrib.auth.models import AbstractUser


# Create your models here.



class User(AbstractUser):
    
    phone = models.CharField(max_length=10)
    address = models.TextField(null=True,blank=True)
    Image  = models.ImageField(upload_to='user/',default='user/1.jpg')
    Techer = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    
    