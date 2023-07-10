from django.db import models
from .user import User
class Education(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    institution           =models.CharField(max_length=100,unique=True,null=True)
    session            =models.CharField(max_length=20,null=True)
    degree          =models.CharField(max_length=50,null=True)
