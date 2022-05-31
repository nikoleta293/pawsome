from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns=[

    path('login/',views.show_login_form,name='login'),
    path('logout/',views.logoutUser,name="logout"),
    path('registration/',views.show_reg_form,name='register'),
    path('forum/',include('Forum.urls'))

]
