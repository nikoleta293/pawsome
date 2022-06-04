import json
import re
from sys import prefix
from turtle import pen
from django.http import JsonResponse
from django.shortcuts import redirect, render
from . forms import RegistrationForm, PetForm, LoginForm
from Users.models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from Pet.models  import Pet


# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def registerPage(request):
    reg_form = RegistrationForm()
    pet_form = PetForm()
   
    context = {'reg_form' : reg_form , 'pet_form' : pet_form}

    if request.method == 'POST':

        reg_form = RegistrationForm(request.POST)
        pet_form = PetForm(request.POST,request.FILES)

        if reg_form.is_valid() and pet_form.is_valid():
         
            reg_form.clean_password()
            reg=reg_form.save()
            pet=pet_form.save()


            return redirect('registration-final' + str(reg.id) + '/' +  str(pet.id) + '/')

        else:
            print(reg_form.errors)
            print(pet_form.errors)
            context = {'reg_form' : reg_form , 'pet_form' : pet_form}
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
