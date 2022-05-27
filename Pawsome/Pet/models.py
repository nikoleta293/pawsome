from asyncio.windows_events import NULL
from distutils.command.upload import upload
from django.db import models
from Users.models import PetOwner

class Pet (models.Model):
    pet_name = models.CharField(max_length=25)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=6)
    kind = models.CharField(max_length=100)
    health_history = models.TextField()
    pet_owner = models.ForeignKey(PetOwner, on_delete = models.SET_NULL,null=True)
    img = models.ImageField(upload_to="D:\Pawsome\Pawsome\Images")
    