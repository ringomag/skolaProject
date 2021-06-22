from django import forms
from django.forms.fields import CharField

class FirstMeetingForm(forms.Form):
    first_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}) )
    last_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}) )
    email=forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':"someone@something.com"}) )

    
    
