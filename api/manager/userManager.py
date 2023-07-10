from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    use_in_migrations=True
    def create_user(self,username,password,**extra_fields):
        if not username:
            raise ValueError("the mobile no. is not given")
        user=self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if not extra_fields.get('is_staff'):
            raise ValueError("Super user")
        self.create_user(username,password,**extra_fields)