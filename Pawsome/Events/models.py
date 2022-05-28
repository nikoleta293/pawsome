from sqlite3 import TimestampFromTicks
from django.db import models
from Users.models import PetOwner, Professional

class Event(models.Models):
    Title= models.TextField
    TimeStamp=models.TimeField
    Description=models.TextField
    Notification=models.BooleanField
    Repeat=models.SmallIntegerField
    pet_owner = models.ForeignKey(PetOwner, on_delete = models.SET_NULL)

class Appointment(Event):
    isDone=models.BooleanField
    professional= models.ForeignKey(Professional, on_delete = models.SET_NULL)