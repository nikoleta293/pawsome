from sqlite3 import TimestampFromTicks
from xmlrpc.client import Boolean
from django.db import models
from django.core.exceptions import ValidationError
  

""" class EventAbstract(models.Model):
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
    end_time = models.DateTimeField() """

class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    #checks for overlap
"""     def check_event(self, fixed_start, fixed_end, new_start, new_end):
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
 """
class Appointment(Events):
    isDone=models.BooleanField
