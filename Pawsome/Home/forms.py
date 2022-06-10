from dataclasses import field
from django.forms import ModelForm,TextInput
from Pet.models import Pet
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.safestring import mark_safe
from Users.models import Professional,Users

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=60,help_text="Required. Add a valid email address")
   
    class Meta:
        model = Users
        fields = {"email","username","password1","password2","role"}
        widgets = {
            'email': TextInput(attrs={'class': 'my_form','id' : 'email'}),
            'username': TextInput(attrs={'class': "my_form",'id' : 'username'}),
            'password1': TextInput(attrs={'class': 'my_form','id' : 'password1'}),
            'password2': TextInput(attrs={'class': 'my_form', 'id' : 'password2'}),
            'role' : forms.Select(attrs = { 'class' : 'myform','id' : 'role'})
            }
    
    
    field_order = ['username', 'email','role','password1','password2']

    
    def clean_password(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password1')

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

        confirm_password = cleaned_data.get('password2')


        if password and confirm_password:
            if password != confirm_password:
                msg = "The two password fields must match."
                self.add_error('password_confirm', msg)
        return cleaned_data

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(getattr(self, field, ''))
        return ' '.join(field_values)

   
    def clean_email(self):
       email  = self.cleaned_data.get('email')
       if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is not unique")
       return email
    

class PetForm(ModelForm):

     class Meta:
        model = Pet
        fields = ['pet_name','age','gender','img']

    


class LoginForm(ModelForm):


     password = forms.CharField(widget=forms.PasswordInput)


     class Meta:
        model = Users
        fields = {'email','password'}

    
     field_order = ['email', 'password']

class VerificationForm(ModelForm):

    class Meta:
        model = Professional
        exclude = ('appointment',
        'is_admin','is_active','is_staff',
        'is_superuser','events','role',
        'last_login','password'
        )

        

    field_order = ['username', 'email','profile_image','AFM',
    'address','telephone','hours','certificate','CV','license']

    def clean(self):
        cd = self.cleaned_data
        cert = cd.get('certificate', None)
        CV = cd.get('CV', None)
        lic = cd.get('license',None)
        if cert is not None and CV is not None and lic is not None:
            main1, sub1 = cert.content_type.split('/')
            main2, sub2 = CV.content_type.split('/')
            main3, sub3 = lic.content_type.split('/')
            if not (main1 in ["application", "octet-stream"] and sub1 == "pdf"):
                return self.add_error('certificate', "Please upload a PDF format")
            if not (main2 in ["application", "octet-stream"] and sub2 == "pdf"):
                return self.add_error('CV', "Please upload a PDF format")
            if not (main3 in ["application", "octet-stream"] and sub3 == "pdf"):
                return self.add_error('license', "Please upload a PDF format")
            return cd




special =(
        ('Vet','Vet'),
        ('pet-trainer','Pet Trainer'),
        ('pet-sitter', 'Pet sitter')
    )







class SpecialityForm(ModelForm):

    speciality = forms.ChoiceField(
        choices=special,
        widget=forms.RadioSelect())

    class Meta:
        model = Professional
        fields = ['speciality']
        
        