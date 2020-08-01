from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Food
from .models import User, Profile
from .forms import UserRegisterForm, UserUpdateForm, UpdatePasswordForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    User = request.user
    select_profile = Profile.objects.get(user__username=User)
    favorites = select_profile.favorites.all()
    context = {
        'favorites': list(favorites)
    }
    return render(request, 'users/profile.html', context)

@login_required
def remove_from_profile(request):
    print("########")
    food_id = str(request.GET.get('foods'))
    food_selected = Food.objects.filter(id=food_id)
    if len(food_selected) == 0:
        response = JsonResponse({"error": "there was an error"})
        response.status_code = 403
        return response
    food_selected = food_selected[0]
    id_current_user = request.user.id
    select_profile = Profile.objects.get(user__id=id_current_user)
    select_profile.favorites.remove(food_selected)
    select_profile.save()
    return JsonResponse({})


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
