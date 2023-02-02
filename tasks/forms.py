from django.forms import ModelForm
from django import forms
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class':'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class':'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class':'form-check'}),
            'project': forms.Select(attrs={'class':'form-select'}),
            'assignee': forms.Select(attrs={'class':'form-select'}),
        }
