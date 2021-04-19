from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class myuser(models.Model):
    phon=models.CharField(max_length=15)
    address=models.CharField(max_length=150)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
