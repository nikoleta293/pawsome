from django.shortcuts import render
from django.views.generic import ListView, DetailView

from Forum.models import Post
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm 


#den exei request giati einai class based view
#to list view vazei ola ta post stin selida
#detail view gia epipleon plhrofories se ena post
class ForumView(ListView):
    model=Post
    template_name = 'Forumpage.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class AddPostView(CreateView):
    model= Post
    form_class = PostForm
    
    #fields = ('author', 'post_time', 'post_text')
 
 