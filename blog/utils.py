from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from users.models import Profile, FoodLike
from .models import Food


def Score(request):
    name = str(request.GET.get('foods'))
    food_selected = Food.objects.get(name=name)
    index_selected = int(request.GET.get('index_selected'))
    id_current_user = request.user.id
    last_score = 0
    select_profile = list(Profile.objects.filter(user__id=id_current_user))[0]
    food_like_user = select_profile.food_likes.filter(name=name)
    if len(list(food_like_user)) == 0:
        food_likes = FoodLike(name=name, score=index_selected)
        food_likes.save()
        select_profile.food_likes.add(food_likes)
    else:
        last_score = list(food_like_user)[0].score
        food_like_user.update(score=index_selected)

    print(index_selected, last_score)

    if index_selected == 1 and last_score > index_selected:
        new_score = -last_score
        food_like_user.update(score=0)
    else:
        new_score = index_selected - last_score

    food_selected.score += new_score
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


def update_profile(request):
    name = str(request.GET.get('foods'))
    food_selected = Food.objects.get(name=name)
    id_current_user = request.user.id
    select_profile = Profile.objects.get(user__id=id_current_user)
    user_favorite = list(select_profile.favorites.all())
    if food_selected not in user_favorite:
        select_profile.favorites.add(food_selected)
    else:
        select_profile.favorites.remove(food_selected)
    select_profile.save()
    return JsonResponse({})
