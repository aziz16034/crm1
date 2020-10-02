from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )




class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields =('type', 'price', 'status', 'description')


class StichingForm(forms.ModelForm):
    class Meta:
        model = Stiching
        fields =('type', 'price', 'status', 'description')



class WeavingForm(forms.ModelForm):
    class Meta:
        model = Weaving
        fields =('type', 'price', 'status', 'description')


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields =('type', 'price', 'status', 'description')



class MaintainForm(forms.ModelForm):
    class Meta:
        model = Maintainance
        fields =('type', 'price', 'status', 'description')

        

