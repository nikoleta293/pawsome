from django.shortcuts import render
from django.views.generic import ListView, DetailView

#from Pawsome.Forum.models import Post
from .models import Post


def show_forum(request):
    model = Post
   # template_name = 'Forumpage.html'
    
  #να βαλω ενα queue για να τα παρω απο τη βαση 