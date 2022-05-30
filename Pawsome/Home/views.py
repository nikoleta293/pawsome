import re
from django.shortcuts import redirect, render
from . forms import RegistrationForm, PetForm, LoginForm
from Users.models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def registerPage(request):
    reg_form = RegistrationForm()
    pet_form = PetForm()
    ok_forms = False    
    context = {'reg_form' : reg_form , 'pet_form' : pet_form , 'ok_forms' : ok_forms}

    if request.method == 'POST' and is_ajax(request=request) == True:
        reg_form = RegistrationForm(instance=request.POST.get('reg_form'))
        pet_form = PetForm(instance=request.POST.get('pet_form'))
        
        ok_forms = True

       
        """ reg_form.fields['username'] = form['username']
        reg_form.fields['email'] = form.get('email')
        reg_form.fields['password1'] = form.get('password1')
        reg_form.fields['password2'] = form.get('password2')

        pet_form.fields['pet_name'] = form.get('pet_name')
        pet_form.fields['age'] = form.get('age')
        pet_form.fields['gender'] = form.get('gender') """
        
        """ reg_form = RegistrationForm(instance=reg_form)
        pet_form = PetForm(instance=pet_form) """
        context = {'reg_form' : reg_form , 'pet_form' : pet_form, 'ok_forms' : ok_forms }
   
        return render(request,'registerPage.html',context)
        

    
    if request.method == 'POST' and is_ajax(request=request) == False :
        reg_form  = RegistrationForm(instance=request.POST)
        pet_form  = PetForm(instance=request.POST)

        if reg_form.is_valid() and pet_form.is_valid():
            reg_form.clean_password()
            reg_form.save()
            pet_form.save()
            redirect('login')

    return render(request,'registerPage.html',context)



def logoutUser():
    pass

def loginPage(request):
    
    login_form = LoginForm()

    context = { 'form' : login_form }

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 
       
        user = authenticate(request,username=email,password=password)

        if user is not None:
            login(request,user)

        else:
            messages.error(request,'Invalid Credentials')
        
    return render(request,'loginPage.html',context)

def home(request):

    return render(request,'homePage.html')
