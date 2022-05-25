from django.shortcuts import redirect, render
from .forms import RegistrationForm,PetForm

# Create your views here.

def show_prof_form(request):
    reg_form = RegistrationForm()
    pet_form = PetForm()
    context = {}

    if request.method == 'POST':
        reg_form  = RegistrationForm(request.POST)
        pet_form  = PetForm(request.POST)
        if reg_form.is_valid() and pet_form.is_valid():
            reg_form.clean_password()
            reg_form.save()
            pet_form.save()
            context = { 'ok_forms' : True }
        
    
    return redirect('loginPage.html')   

        


