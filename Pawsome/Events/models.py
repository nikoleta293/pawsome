from sqlite3 import TimestampFromTicks
from xmlrpc.client import Boolean
from django.db import models
from Users.models import PetOwner, Professional
from django.core.exceptions import ValidationError
from Pawsome.Users.models import Users

class Event(models.Models):
    Title= models.TextField
    TimeStamp=models.TimeField
    Description=models.TextField
    Notification=models.BooleanField
    Repeat=models.SmallIntegerField
    pet_owner = models.ForeignKey(PetOwner, on_delete = models.SET_NULL)

class EventAbstract(models.Model):
    #Event abstract model

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Events(EventAbstract):

    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=200)
    notification = models.Boolean(default=False)
    repeat = models.Boolean(default=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    #checks for overlap
    def check_event(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
 
        return overlap


    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending hour must be after the starting hour')

        events = Events.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
class Appointment(Event):
    isDone=models.BooleanField
    professional= models.ForeignKey(Professional, on_delete = models.SET_NULL)
