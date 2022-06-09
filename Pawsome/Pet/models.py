from django.db import models
from Users.models import PetOwner

# Create your models here.

from Users.models import PetOwner

class Pet (models.Model):
    pet_owner = models.OneToOneField(PetOwner,on_delete=models.CASCADE,default=None)
    pet_name = models.CharField(max_length=25)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=6)
    kind = models.CharField(max_length=100)
    health_history = models.TextField()
    img = models.ImageField(null=True,blank=True,default="../Images/logo.png",upload_to='Images/')


    def __str__(self):
        return self.pet_name