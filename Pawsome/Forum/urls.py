from django.urls import path
from . import views 
from .views import ForumView, AddPostView
from .views import AddPostView
urlpatterns = [
    
     path('forum/',ForumView.as_view(), name='forum')
     #path('add_ost/',AddPostView.as_view(), name='addpost')
] #to 2o path den einai accesable parolo poy to ekana import