from django import forms
from .models import Post
from django.forms import TextInput

class PostForm (forms.ModelForm):
    class Meta: 
        model=Post 
        fields = ('author','post_text')
        
        widgets = {
            'author': TextInput(attrs={'class': 'post_form','id' : 'author'}),
            #'post_time': forms.forms.DateTimeField(, required=False) 
            'post_text': TextInput(attrs={'class': 'post_form','id' : 'email'}),
            
            
        }     
       
      