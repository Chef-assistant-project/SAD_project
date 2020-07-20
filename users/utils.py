from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from users.models import Profile, FoodLike
from .models import Food

def remove_from_profile(request):
    print("########")
    name = str(request.GET.get('foods'))
    food_selected = Food.objects.get(name=name)
    id_current_user = request.user.id
    select_profile = Profile.objects.get(user__id=id_current_user)
    select_profile.favorites.remove(food_selected)
    select_profile.save()
    return JsonResponse({})
