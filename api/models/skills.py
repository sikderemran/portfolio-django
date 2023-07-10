from django.db import models
from .user import User
class Skill(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name           =models.CharField(max_length=20,null=True)
 
