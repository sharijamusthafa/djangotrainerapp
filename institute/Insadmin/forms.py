from django.forms import ModelForm

from django import forms
from Insadmin.models import InstituteDetails,SkillModel,filterskill




class InstituteForm(ModelForm):
    class Meta:
        model=InstituteDetails
        fields="__all__"


class skillform(ModelForm):
    class Meta:
        model=SkillModel
        fields="__all__"

class filterform(ModelForm):
    class Meta:
        model=filterskill
        fields="__all__"