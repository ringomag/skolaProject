from django import forms
from django.forms import ModelForm
from .models import Blog
from ckeditor.fields import RichTextField

class FirstMeetingForm(forms.Form):
    first_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}) )
    last_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}) )
    email=forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':"someone@something.com"}) )

    
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'firstName' : forms.TextInput(attrs={'class':'form-control'}),
            'lastName' : forms.TextInput(attrs={'class':'form-control'}),
            'summary' : forms.TextInput(attrs={'class':'form-control'}),
            
        }
            
