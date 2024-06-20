from django.db import models

# Create your models here.
class User(AbstractUser):
    usertype=models.CharField(max_length=20)
    phone=models.BigIntegerField(max_length=10)
    
