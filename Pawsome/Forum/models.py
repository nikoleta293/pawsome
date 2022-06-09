from asyncio.windows_events import NULL
from sqlite3 import Timestamp
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from Users.models import Users

class Post (models.Model):
    author = models.ForeignKey(Users,on_delete=models.CASCADE,default=None) 
    post_time = models.DateTimeField(auto_now_add=True)
    post_text = models.TextField(max_length=200)
    
    def __str__(self):
        return self.post_text 
    
    
    def get_absolute_url(self):
        return reverse('forum') 
    