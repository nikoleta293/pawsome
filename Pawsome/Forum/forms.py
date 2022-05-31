from django import forms
from .models import Post

class PostForm (forms.ModelForm):
    class Meta: 
        model=Post 
        fields = ('author', 'post_time', 'post_text')
        
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control' }), 
            #'post_time': forms.forms.DateTimeField(, required=False) 
            'post_text': forms.CharField({'required': True},{'size': '200'})
            
            
        }     
       
      