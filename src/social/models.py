from django.db import models

# Create your models here.
class User(models.Model):
    
    
    def __str__(self):
        return self.username
    
    
class Profile(models.Model):
    
    user=models.ForiegnKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="user")
    