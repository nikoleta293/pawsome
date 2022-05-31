import json
import re
from sys import prefix
from django.http import JsonResponse
from django.shortcuts import redirect, render
from . forms import RegistrationForm, PetForm, LoginForm
from Users.models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize


# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def registerPage(request):
    reg_form = RegistrationForm()
    pet_form = PetForm()
   
    context = {'reg_form' : reg_form , 'pet_form' : pet_form}

    if request.method == 'POST':

        reg_form = RegistrationForm(request.POST)
        pet_form = PetForm(request.POST)

        if reg_form.is_valid() and pet_form.is_valid():
         
            reg_form = json.dumps(reg_form.cleaned_data)
            pet_form = json.dumps(pet_form.cleaned_data)
            
            request.session['reg_form'] = reg_form
            request.session['pet_form'] = pet_form

            return redirect('final-register')

            
        
    

    return render(request,'registerPage.html',context)


def registerAll(request):

    reg_form = RegistrationForm(json.loads(request.session['reg_form']))
    pet_form = PetForm(json.loads(request.session['pet_form']))

    """ reg_form = request.session['reg_form']
    pet_form = request.session['pet_form'] """

    context = {'reg_form' : reg_form , 'pet_form' : pet_form}


    if request.method == 'POST':
        
        if reg_form.is_valid() and pet_form.is_valid():
            reg_form.clean_password()
            reg_form.save()
            pet_form.save()
            redirect('login')
    
    return render(request,'final_register.html',context)



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
