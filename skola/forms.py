from django import forms
from django.forms.fields import CharField

class FirstMeeting(forms.Form):
    firstName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    lastName=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"someone@something.com"}))
    
