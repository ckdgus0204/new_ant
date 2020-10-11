from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models 
class UserManager(BaseUserManager):    
    
    
    
    def create_user(self, username,account,date,name , password):        
        user = self.model(            
            name = name,
            account= account,
            date=date,
            username=username,   
               
        )        
        user.set_password(password)
        user.save(using=self._db)        
        return user     
    def create_superuser(self,name,account,date, username,password ):        
        user = self.create_user(            
            name = name,
            password=password,
            account= account,
            date=date,
            username=username,    
        )        
        user.set_password(password)
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 
class User(AbstractBaseUser,PermissionsMixin):    
    username = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        primary_key=True,
    )
  
    name = models.CharField(        
        max_length=20,
        null=False,          
    )    
    account = models.FloatField(
    )     
    date = models.DateTimeField(
        auto_now_add=True,
    )
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=True)    
    is_superuser = models.BooleanField(default=True)    
    is_staff = models.BooleanField(default=True)    


    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['name','account','date']
    object = UserManager()