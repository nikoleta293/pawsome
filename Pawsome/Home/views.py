from django.shortcuts import redirect, render
from . forms import RegistrationForm,PetForm,LoginForm
from Users.models import Users
from django.contrib import messages

# Create your views here.

def show_reg_form(request):
    reg_form = RegistrationForm()
    pet_form = PetForm()
    pet_ok = request.POST.get('pet_ok')
    #context = {'ok_forms' : False}
    ok_forms = False

    if request.method == 'POST' and request.is_ajax():
        data = request.POST.get('data')
        form = request.POST.get('form')
        ok_forms = data.get('pet_ok')
        
        reg_form.fields['username'] = form.get('username')
        reg_form.fields['email'] = form.get('email')
        reg_form.fields['password'] = form.get('password')
        reg_form.fields['password_confirm'] = form.get('password_confirm')

        pet_form.fields['name'] = form.get('name')
        pet_form.fields['age'] = form.get('age')
        pet_form.fields['kind'] = form.get('kind')
        pet_form.fields['img'] = form.get('img')



    if request.method == 'POST' and ok_forms == True:
        reg_form  = RegistrationForm(request.POST)
        pet_form  = PetForm(request.POST)

        if reg_form.is_valid() and pet_form.is_valid():
            reg_form.clean_password()
            reg_form.save()
            pet_form.save()
        
    
    return redirect('loginPage.html')   

        


def logoutUser():
    pass

def show_login_form(request):
    login_form = LoginForm()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pasword') 
       
       
        try:
            user = Users.objects.get(email=email)

        except:
            messages.error(request,'User does not exist')


        if user.get('password') == password:
            