from django.urls import path 
from .views import FormAndListView


urlpatterns = [
    
     path('',FormAndListView.as_view(), name='forum'),
] 