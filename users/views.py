from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import User, Profile
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
    User = request.user
    selectProfile = Profile.objects.filter(user__username=User)
    for x in selectProfile:
        favorites = x.favorites.all()
    context = {
        'favorites': list(favorites)
    }
    return render(request, 'users/profile.html', context)


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

def login(request):
    return render(request, 'users/login.html')


def logout(request):
    return render(request, 'users/logout.html')