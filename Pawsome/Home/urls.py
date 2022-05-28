from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[

    path('',views.home,name="home"),
    path('login/',views.show_login_form,name='login'),
    path('logout/',views.logoutUser,name="logout"),
    path('registration/',views.show_reg_form,name='register')


]