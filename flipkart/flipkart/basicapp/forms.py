from django import forms
from django.contrib.auth.models import User
from basicapp import models

class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('Username','First name','Last name','Email address','Password')
        widgets = {
            'Username':forms.CharField(attrs={'class':'user_name'}),
            'First name':forms.CharField(attrs={'class':'First_name'}),
            'Last name':forms.CharField(attrs={'class':'First_name'}),
            'Email address':forms.EmailInput(attrs={'class':'First_name'}),
            'Password':forms.PasswordInput(attrs={'class':'Password'}),
        }  

