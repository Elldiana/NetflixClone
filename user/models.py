from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class CustomUser(AbstractUser):
    birth_date = models.DateField(verbose_name='Dogum yılı',null=True)
    phone = models.CharField(max_length=11,null=True)

    def profilleri_say(self):
        return self.profile_set.all().count()
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Profile(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_pic')
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name