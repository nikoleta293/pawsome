from django.urls import path
from . import views 
#from .views import ForumView, AddPostView
#from .views import AddPostView

from .views import FormAndListView

urlpatterns = [
    
     path('',FormAndListView.as_view(), name='forum'),
     #path('forum<str:pk>/',AddPostView.as_view(), name='add_post')
] 