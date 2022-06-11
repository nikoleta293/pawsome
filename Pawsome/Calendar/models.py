from sqlite3 import TimestampFromTicks
from xmlrpc.client import Boolean
from django.db import models
from django.core.exceptions import ValidationError
  

class EventAbstract(models.Model):
    #Event abstract model

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Events(EventAbstract):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=200)
    notification = models.BooleanField(default=False)
    repeat = models.BooleanField(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Appointment(Events):
    isDone=models.BooleanField
