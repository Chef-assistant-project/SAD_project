from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from users.models import Profile
from .models import Food


def Score(request):
    name = str(request.GET.get('foods'))
    food_selected = Food.objects.get(name=name)
    action = str(request.GET.get('action'))
    index_selected = int(request.GET.get('index_selected'))

    ## for sogand (bug dare id bezar):
    # User = request.user
    # selectProfile = Profile.objects.get(user__username=User)

    if action == 'add':
        food_selected.score += index_selected
    elif action == 'remove':
        food_selected.score -= index_selected
    food_selected.save()
    return JsonResponse({'likes': food_selected.score})


def direct_search(selected_food):
    match = []
    for _ in Food.objects.all():
        if len(selected_food) != 0:
            match = Food.objects.filter(name__icontains=selected_food)
        else:
            match = []

    return match


def UpdateProfile(request):
    name = str(request.GET.get('foods'))
    food_selected = Food.objects.get(name=name)
    action = str(request.GET.get('action'))
    User = request.user
    select_profile = Profile.objects.get(user__username=User)
    if action == 'add':
        select_profile.favorites.add(food_selected)
    elif action == 'remove':
        select_profile.favorites.remove(food_selected)
    select_profile.save()
    return JsonResponse({})
