from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from trainer.models import TrainerProfile,filterskill,SkillModel



class TrainerRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={

            "first_name": forms.TextInput(attrs={"class": "form-control text-white-50 bg-dark"}),
            "last_name": forms.TextInput(attrs={"class": "form-control text-white-50 bg-dark"}),
            "email": forms.TextInput(attrs={"class": "form-control text-white-50 bg-dark"}),
            "username": forms.TextInput(attrs={"class": "form-control text-white-50 bg-dark"}),
            "password1": forms.TextInput(attrs={"class": "form-control text-white-50 bg-dark"}),
            "password2": forms.TextInput(attrs={"class": "form-control text-white-50 bg-dark"}),
        }

class TrainerLoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),max_length=100)
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),max_length=120)

class skillform(ModelForm):
    class Meta:
        model=SkillModel
        fields="__all__"



class trainerProfileForm(ModelForm):
    class Meta:
        model=TrainerProfile
        fields="__all__"


class applyform(forms.Form):
    name=forms.CharField(max_length=120)

class filterform(ModelForm):
    class Meta:
        model=filterskill
        fields="__all__"