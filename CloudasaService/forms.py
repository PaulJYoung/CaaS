from .models import ContactUs
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    firstname = forms.CharField(widget=forms.Textarea(attrs={'class': 'formlblbox', 'cols': 100, 'rows': 1}),max_length=100)
    surname = forms.CharField(widget=forms.Textarea(attrs={'class': 'formlblbox', 'cols': 100, 'rows': 1}),max_length=100)
    emailaddr = forms.CharField(widget=forms.Textarea(attrs={'class': 'formlblbox', 'cols': 100, 'rows': 1}),max_length=100)
    post = forms.CharField(widget=forms.Textarea(attrs={'class': 'formtxtbox', 'cols': 100, 'rows': 20}), max_length=2000)
    
