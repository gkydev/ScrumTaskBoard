from django import forms
from django.forms import ModelForm

from .models import *

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['job_title', 'job_desc', 'job_notes']

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ["task_desc"]

