from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'owner': forms.Select(attrs={'class':'form-select'}),
            'team': forms.Select(attrs={'class':'form-select'}),
        }
