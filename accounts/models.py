from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    ROLE_CHOICES = [
        ('admin','Admin'),
        ('doctor','Doctor'),
        ('patient','Patient')       
    ]
        
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name= 'profile')
    
    role = models.CharField(max_length=20
                            ,choices=ROLE_CHOICES
                            )

    profile_image = models.ImageField(
                    upload_to='profiles/',
                    blank= True,
                    null= True
                    )
    
    
    def __str__(self):
        return f' {self.user.username},{self.role}'
    