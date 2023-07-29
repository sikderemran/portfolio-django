from django.db import models
from .user import User
class Experience(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    session           =models.CharField(max_length=20,null=True)
    company           =models.CharField(max_length=100,null=True)
    title           =models.CharField(max_length=100,null=True)
 
