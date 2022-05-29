from django.urls import path
from . import views 

urlpatterns = [
    
     path('forum/',views.show_forum,name='forum')
]