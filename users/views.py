from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import User
from .forms import UserRegisterForm, UserUpdateForm, UpdatePasswordForm


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
def profile(request):
    return render(request, 'users/profile.html')


class ChangeEmail(generic.UpdateView):
    model = User
    fields = ['email']
    template_name = 'users/changeEmail.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


class ChangePassword(generic.UpdateView):
    model = User
    template_name = 'users/changePassword.html'
    success_url = reverse_lazy('login')
    form_class = UpdatePasswordForm

    def get_object(self, queryset=None):
        return self.request.user
