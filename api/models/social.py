from django.db import models
from .user import User
class Social(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name           =models.CharField(max_length=50,null=True)
    link           =models.CharField(max_length=50,null=True)
    icon           =models.CharField(max_length=50,null=True)
 
