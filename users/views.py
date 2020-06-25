from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def UpdateUser(request, typeOfRequest):
    methodIsPost = False
    if typeOfRequest == "profile":
        return render(request, 'users/profile.html')
    elif typeOfRequest == "changeEmail":
        if request.method == 'POST':
            methodIsPost = True
            form = UserUpdateForm(request.POST, instance=request.user)
    elif typeOfRequest == "changePassword":
        if request.method == 'POST':
            methodIsPost = True
            form = PasswordChangeForm(data=request.POST, user=request.user)
    if methodIsPost:
        if form.is_valid():
            form.save()
            if typeOfRequest == "changePassword":
                update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile' ,typeOfRequest = "profile")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        if typeOfRequest == "changeEmail":
            form = UserUpdateForm(instance=request.user)
        else:
            form = PasswordChangeForm(request.user)
    if typeOfRequest == "changeEmail":
        return render(request, 'users/changeEmail.html', {'form': form})
    return render(request, 'users/changePassword.html', {'form': form})
