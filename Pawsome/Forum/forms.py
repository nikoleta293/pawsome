from django import forms
from .models import Post
from django.forms import TextInput

class PostForm (forms.ModelForm):
    class Meta: 
        model=Post 
        fields = ['post_text']
        
        widgets = {
            'post_text': TextInput(attrs={'class': 'post_form','id' : 'email'})
            
        }     
       
      