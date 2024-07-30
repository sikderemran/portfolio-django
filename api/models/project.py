from django.db import models
from .user import User
class Project(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image           =models.ImageField(upload_to='uploaddir/images/')
    title           =models.CharField(max_length=100,null=True)
    description           =models.CharField(max_length=1000,null=True)
    tech_used           =models.CharField(max_length=300,null=True)
    link           =models.CharField(max_length=50,null=True)
    project_order           =models.IntegerField(null=True)
 
