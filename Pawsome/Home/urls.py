from unicodedata import name
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('registration/',views.registerPage,name='register'),
    path('registration-final/',views.registerAll,name="final-register"),
    path('forum/',include('Forum.urls')),
    path('',views.home,name='home'),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('Calendar/',include('Calendar.urls'))


]
