from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Created For %s!' % username)
            return redirect('homepage')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def profile(request):
    args = {'user': request.user }
    return render(request, 'user/profile.html', args)

def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid:
            form.save()
            return redirect('/user/profile')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form': form}
        return render(request, 'user/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(cleaned_data = request.POST, user = request.user)
        if form.is_valid:
            form.save()
            return redirect('/user/profile')
    else:
            form = PasswordChangeForm(user = request.user)
            args = {'form': form, 'username' : request.user.username}
            return render(requser_logoutuest, 'user/change_password.html', args)
