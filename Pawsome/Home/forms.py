from django.forms import ModelForm,TextInput
from Users.models import Users
from Pet.models import Pet
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=60,help_text="Required. Add a valid email address")
   
    class Meta:
        model = Users
        fields = {"email","username","password1","password2"}
        widgets = {
            'email': TextInput(attrs={'class': 'my_form','id' : 'email'}),
            'username': TextInput(attrs={'class': "my_form",'id' : 'username'}),
            'password1': TextInput(attrs={'class': 'my_form','id' : 'password1'}),
            'password2': TextInput(attrs={'class': 'my_form', 'id' : 'password2'})
            }
    
    
    field_order = ['username', 'email', 'password1','password2']

    
    def clean_password(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')

        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' %(str(min_length))
            self.add_error('password', msg)

        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)

        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)

        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)

        confirm_password = cleaned_data.get('confirm_password')


        if password and confirm_password:
            if password != confirm_password:
                msg = "The two password fields must match."
                self.add_error('password_confirm', msg)
        return cleaned_data

    def __str__(self):
        field_values = []
        for field in self.meta.get_all_field_names():
            field_values.append(getattr(self, field, ''))
        return ' '.join(field_values)
    

class PetForm(ModelForm):

     class Meta:
        model = Pet
        fields = ['pet_name','age','gender','img']



class LoginForm(ModelForm):

     class Meta:
        model = Users
        fields = ['email','password']

