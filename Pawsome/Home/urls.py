from unicodedata import name
from django.urls import path, include
from django.views import View
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('registration/',views.registerPage,name='register'),
    path('registration/registration-final<str:pk>/<str:pk2>/',views.registerAll,name="final-register"),
    path('forum/',include('Forum.urls')),
    path('',views.home,name='home'),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("registration/verification<str:pk3>/<str:pk4>/",views.verification,name="verification"),
    path("org-verify/",views.org_verify,name="org-verify"),
    path('deleteUser/<str:pk5>/',views.delete_user,name="deleteUser")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
