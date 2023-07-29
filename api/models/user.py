from django.db import models
from django.contrib.auth.models import AbstractUser
from ..manager.userManager import UserManager

class User(AbstractUser):
    username           =models.CharField(max_length=100,unique=True,null=True)
    designation              =models.CharField(max_length=50,null=True)
    image              =models.ImageField(upload_to='uploaddir/images/',null=True)
    about            =models.CharField(max_length=1000,null=True)
    resume              =models.FileField(upload_to='uploaddir/resume/',null=True)
    phone              =models.CharField(max_length=20,null=True)
    password            =models.CharField(max_length=255,null=True)
    created_at          =models.DateTimeField(auto_now_add=True)
    updated_at          =models.DateTimeField(auto_now=True)

    
    objects=UserManager()
    USERNAME_FIELD='username'


