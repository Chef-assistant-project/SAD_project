from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from users.models import Profile, FoodLike
from .models import Food


def direct_search(selected_food):
    match = []
    for _ in Food.objects.all():
        if len(selected_food) != 0:
            match = Food.objects.filter(name__icontains=selected_food)
        else:
            match = []
    return match



