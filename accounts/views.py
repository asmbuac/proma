from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from .models import UserProfile, Team
from .forms import LoginForm, SignUpForm, UserProfileForm, EditUserProfileForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error("password", "The password is incorrect")
                form.add_error("username", "The username does not exist")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                form.add_error("username", "This username is already taken")
            elif User.objects.filter(email=form.cleaned_data["email"]).exists():
                form.add_error("email", "This email has already been registered")
            elif password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                login(request, user)
                return redirect("home")
            else:
                form.add_error("password", "The passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


@login_required
def view_my_profile(request):
    return render(request, "accounts/user-profile/mine.html")


@login_required
def view_user_profile(request, id):
    profile = get_object_or_404(UserProfile, id=id)
    context = {
        "profile": profile,
    }
    return render(request, "accounts/user-profile/view.html", context)


@login_required
def edit_user_profile(request):
    if request.method == "POST":
        uform = EditUserProfileForm(request.POST, instance=request.user)
        pform = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if uform.is_valid() and pform.is_valid():
            user_form = uform.save()
            profile = pform.save(False)
            profile.user = user_form
            profile.save()
            return redirect("view_my_profile")
        else:
            uform.add_error("password", "The passwords do not match")
    else:
        uform = EditUserProfileForm(instance=request.user)
        try:
            pform = UserProfileForm(instance=request.user.userprofile)
        except UserProfile.DoesNotExist:
            pform = UserProfileForm()
    args = {}
    args.update(csrf(request))
    args['uform'] = uform
    args['pform'] = pform
    return render(request, "accounts/user-profile/edit.html", args)
