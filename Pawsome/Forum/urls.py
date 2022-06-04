from django.urls import path
from . import views 
from .views import ForumView, AddPostView
from .views import AddPostView
urlpatterns = [
    
     path('',ForumView.as_view(), name='forum'),
] 