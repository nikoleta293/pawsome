from distutils.command.sdist import sdist
import json
import re
from sys import prefix
from turtle import pen
from django.http import JsonResponse
from django.shortcuts import redirect, render

from Users.models import PetOwner,Professional
from . forms import RegistrationForm, PetForm, LoginForm,SpecialityForm, VerificationForm
from Users.models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from Pet.models  import Pet


import logging

logger = logging.getLogger(__name__)


# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def registerPage(request):
    reg_form = RegistrationForm()
    pet_form = PetForm()
    special_form = SpecialityForm()
   
    context = {'reg_form' : reg_form , 'pet_form' : pet_form,'special_form' : special_form}

    if request.method == 'POST':

        reg_form = RegistrationForm(request.POST)
        pet_form = PetForm(request.POST,request.FILES)
        special_form = SpecialityForm(request.POST)

        if reg_form.is_valid() and special_form.is_valid():
            
            reg_form.clean_password()
            reg=reg_form.save()
            special = special_form.cleaned_data['speciality']
            logger.warning('Platform is running at risk')
            return redirect('verification' + str(reg.id) + '/' + str(special) + '/')

        elif reg_form.is_valid() and pet_form.is_valid():
            
            reg_form.clean_password()
            reg=reg_form.save()
            pet_obj=pet_form.save()
            pet_obj.pet_owner = reg
            pet=pet_obj.save()
            return redirect('registration-final' + str(reg.id) + '/' +  str(pet.id) + '/')
                
        
           
        else:
            pet_form = PetForm()
            special_form = SpecialityForm()
            context = {'reg_form' : reg_form , 'pet_form' : pet_form,'special_form' : special_form}
            return render(request,'registerPage.html',context)

            
    

    return render(request,'registerPage.html',context)


def registerAll(request,pk,pk2):

    reg_form = RegistrationForm()
    pet_form = PetForm()
   
   
    if request.method == 'POST':

        reg_form = RegistrationForm(request.POST)
        pet_form = PetForm(request.POST,request.FILES)
        
        if reg_form.is_valid() and pet_form.is_valid():
            reg_form.clean_password()
            reg_form.save()
            pet_form.save()
            redirect('login')

    elif request.method == 'GET':
        user = Users.objects.get(id=pk)
        pet = Pet.objects.get(id=pk2)
        reg_form = RegistrationForm(instance=user)
        pet_form = PetForm(instance=pet)
        context = { 'reg_form' : reg_form, 'pet_form' : pet_form,'user' : user , 'pet' : pet}

        return render(request,'final_register.html',context)
    
    return redirect('login')



def loginPage(request):
    
    login_form = LoginForm()

    context = { 'form' : login_form }

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 
       
        user = authenticate(request,username=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.error(request,'Invalid Credentials')
        
    return render(request,'loginPage.html',context)

def home(request):

    return render(request,'homePage.html')

def verification(request,pk3,pk4):
    verify_form = VerificationForm()


    if request.method == 'GET':
        user = Users.objects.get(id=pk3)
        user.password = ''
        speciality = pk4
        verify_form = VerificationForm(instance=user)
        verify_form.fields['speciality'].initial = speciality
        verify_form.fields['speciality'].widget.attrs['readonly'] = True
        

        context = { 'verify_form' : verify_form , 'id' : pk3, 'speciality' : pk4}

        return render(request,'certification.html',context)

    elif request.method == 'POST':
        verify_form = VerificationForm(request.POST,request.FILES)


        if verify_form.is_valid():
            verify_form.save()
            return redirect('login')
        else:
            verify_form.clean()
            context = { 'verify_form' : verify_form , 'id' : pk3, 'speciality' : pk4}
            return render(request,'certification.html',context)


    return render(request,'certification.html',context)





def delete_user(request,pk5):

    if request.method == 'GET':
        u = Users.objects.get(id=pk5)
        u.delete()
        return redirect('login')


def org_verify(requst):
    pass
