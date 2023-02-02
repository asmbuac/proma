from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        error_messages={
            "unique": ("This username is already taken")
        }
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(
        max_length=150,
        error_messages={
            "unique": ("This email has already been registered")
        }
    )


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields["level"].choices = (
            ('team', 'team leader'),
            ('member', 'team member')
        )

    class Meta:
        model = UserProfile
        exclude = (
            "user",
        )
        widgets = {
            "picture": forms.FileInput(attrs={'class':'form-control'}),
            "team": forms.Select(attrs={'class':'form-select'}),
            "level": forms.Select(attrs={'class':'form-select'}),
        }


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )
        widgets = {
            "username": forms.TextInput(attrs={'class':'form-control'}),
            "first_name": forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.EmailInput(attrs={'class':'form-control'}),
        }
