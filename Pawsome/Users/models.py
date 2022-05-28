from contextlib import nullcontext
from distutils.command import upload
from re import T
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from . managers import CustomUserManager

def get_profile_image_filepath(self,filename):
    return f'../Images/profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "../Images/logo_tranparent.png"


class Users (AbstractBaseUser): 
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True,unique=True,verbose_name='email')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image =models.ImageField(max_length=255,upload_to="D:\1Mentor\Altair\CEID\Εξεταστική 2021-2022\Β' Εξάμηνο\Τεχνολογία Λογισμικού\Project\Pawsome\pawsome\Pawsome\Images",null=True,blank=True,default="D:\1Mentor\Altair\CEID\Εξεταστική 2021-2022\Β' Εξάμηνο\Τεχνολογία Λογισμικού\Project\Pawsome\pawsome\Pawsome\Images\logo_transparent.png")
    confirm_password = models.CharField(max_length=200)

    exclude = ('is_admin','is_active','is_staff','is_superuser')


    Roles =(
    ('org','Organizations'),
    ('pros','Professional'),
    ('pet-owner','Pet Owner')
    )
    role = models.CharField(max_length=50, choices=Roles)
   
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    def has_perm (self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_image/{self.pk}/'):]


class PetOwner (Users):
    pet_name = models.CharField(max_length=50)
    owner_email = models.ForeignKey('Users', on_delete=models.CASCADE,related_name='own_email')
    #appointmentList
    
class Professional (Users):
    AFM = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    hours = models.TimeField(auto_now=False, auto_now_add=False)
    telephone = models.CharField(max_length=12)
    prof_email = models.ForeignKey('Users', on_delete=models.CASCADE,related_name='pro_email')
    #appointmentList
    certificate= models.FileField()
    CV = models.FileField()
    license = models.FileField()
    
    
    
class Organizations(Users):
    AFM = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    hours = models.TimeField(auto_now=False, auto_now_add=False)
    telephone = models.CharField(max_length=12)
    org_email = models.ForeignKey('Users', on_delete=models.CASCADE,related_name='organization_email')

   

    