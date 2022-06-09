from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.views.generic.edit import BaseCreateView
from .models import Post

from django.views.generic.list import BaseListView

from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm 
from django.views.generic.base import TemplateResponseMixin


""" class ForumView(ListView):
    model=Post
    template_name = 'Forumpage.html'

    

class AddPostView(CreateView):
    model= Post
    form_class = PostForm
    template_name ='AddPost.html'
    fields = ['post_text']
 
 """


class FormAndListView(BaseCreateView, BaseListView, TemplateResponseMixin):
    
    model = Post

    fields = ['post_text']

    template_name = 'Forumpage.html'

    
    def get(self, request, *args, **kwargs):
        formView = BaseCreateView.get(self, request, *args, **kwargs)
        listView = BaseListView.get(self, request, *args, **kwargs)
        formData = formView.context_data['form']
        listData = listView.context_data['object_list']
        return render(request,'ForumPage.html', {'form' : formData, 'all_posts' : listData})