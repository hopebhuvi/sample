from django import forms
from django.db import models
from bhuvi1.models import Emp
from bhuvi1.models import State
from bhuvi1.models import District

class Empform(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"

class Stateform(forms.ModelForm):
    class Meta:
        model=State
        fields="__all__"

class Districtform(forms.ModelForm):
    class Meta:
        model=District
        fields="__all__"
     