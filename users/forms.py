from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    
    class Meta :
        model = Task
        fields = '__all__'