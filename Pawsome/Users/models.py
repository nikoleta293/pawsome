from django.db import models
from django.contrib.auth.models import User


class Users (models.Model): 
    username = models.CharField(max_length=50)
    password = models.CharField()
    email = models.EmailField(primary_key=True)
    Roles =('organizations','professional','pet-owner')
    role = models.CharField(max_length=50, choices=Roles)
   
    def __str__(self):
        return self.email

class PetOwner (Users):
    pet_name = models.CharField(max_length=50)
    owner_email = models.ForeignKey(Users, on_delete=models.CASCADE)
    #appointmentList
    
class Professional (Users):
    AFM = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    hours = models.TimeField(auto_now=False, auto_now_add=False)
    telephone = models.CharField(max_length=12)
    prof_email = models.ForeignKey(Users, on_delete=models.CASCADE)
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
    org_email = models.ForeignKey(Users, on_delete=models.CASCADE)

   

    