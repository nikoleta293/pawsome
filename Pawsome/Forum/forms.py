from django import forms
from .models import Post
from django.forms import TextInput

class PostForm (forms.ModelForm):
    class Meta: 
        model=Post 
        fields = ['post_text']



    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['post_text'].widget.attrs['cols'] = 10
        self.fields['post_text'].widget.attrs['rows'] = 20  
       
    #def clean ()  