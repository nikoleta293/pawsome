from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[

    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name="logout"),
    path('registration/',views.registerPage,name='register')


]