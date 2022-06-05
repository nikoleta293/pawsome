from django.shortcuts import render
from django.views.generic.list import BaseListView
from django.views.generic.edit import BaseCreateView
from django.views.generic.base import TemplateResponseMixin
from .models import Post


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
 
 