from asyncio.windows_events import NULL
from sqlite3 import Timestamp
from tkinter import CASCADE
from django.db import models
from django.urls import reverse

class Post (models.Model): 
    post_time = models.DateTimeField(auto_now_add=True)
    post_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.post_text + ' | ' + self.author + ' | ' +self.post_time
    
    #methodos poy se epistrefei sto forum
    def get_absolute_url(self):
        return reverse('forum', args=(str(self.id))) #id=primarykey
    