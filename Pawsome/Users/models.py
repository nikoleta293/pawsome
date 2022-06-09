from contextlib import nullcontext
from distutils.command import upload
from email.policy import default
from re import T
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from Calendar.models import Appointment,Events
import datetime
from uuid import uuid4

from . managers import CustomUserManager

def get_profile_image_filepath(self,filename):
    return f'../Images/profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "../Images/logo_tranparent.png"


class Users (AbstractBaseUser): 
    username = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True,editable=False)
    email = models.EmailField(unique=True,verbose_name='email')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image =models.ImageField(max_length=255,upload_to="logo_transparent.png",default='Logo-small.png')
    events = models.ManyToManyField(Events)


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

    def create_id():
        now = datetime.datetime.now()
        return str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7]

class PetOwner (Users):
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True)
    
class Professional (Users):
    AFM = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    hours = models.TimeField(default='00:00')
    telephone = models.CharField(max_length=12)
    appointment =  models.ManyToManyField(Appointment)
    #appointmentList
    certificate= models.FileField()
    CV = models.FileField()

    special =(
        ('Vet','Vet'),
        ('pet-trainer','Pet Trainer'),
        ('pet-sitter', 'Pet sitter')
    )
    speciality = models.CharField(max_length=50, choices=special)


    license = models.FileField()
    
    
    
class Organizations(Users):
    AFM = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    hours = models.TimeField(auto_now=False, auto_now_add=False)
    telephone = models.CharField(max_length=12)

   

    