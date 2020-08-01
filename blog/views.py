from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render
from blog import utils
from .models import Food
from .forms import ChooseIngredientsForm, FilterTypesForm
from django.http import JsonResponse
from users.models import Profile, FoodLike


def home(request):
    best_food_score = Food.objects.order_by('-score')[:3]
    context = {
        'best_food_score': best_food_score,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    food_selected_with_selected_ingredient = []
    chosen_ingredient = []
    previous_ingredients = []
    match = []
    cuisine = "all"
    diet = "all"
    meal_type = "all"
    site = "all"

    if request.method == "POST":
        match = utils.direct_search(str(request.POST.get('title') or "").strip())

    filter_types_form = FilterTypesForm(request.POST or None)
    ingredients_form = ChooseIngredientsForm(request.POST or None)

    # filter attribute:
    if request.method == "POST" and filter_types_form.is_valid():
        if "diet" in request.POST:
            diet = request.POST.get("diet")
        if "cuisine" in request.POST:
            cuisine = request.POST.get("cuisine")
        if "mealType" in request.POST:
            meal_type = request.POST.get("mealType")
        if "site" in request.POST:
            site = request.POST.get("site")

    # filter ingredient:
    if request.method == "POST" and ingredients_form.is_valid():
        for form in ingredients_form:
            if form.name in request.POST:
                for selected_ingredient in request.POST.getlist(form.name):
                    previous_ingredients.append(selected_ingredient)
                    food_with_selected_ingredient = Food.objects.filter(ingredients__name=selected_ingredient)
                    if diet != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(diet=diet)
                    if cuisine != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(cuisine=cuisine)
                    if meal_type != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(mealType=meal_type)
                    if site != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(url__icontains=site)
                    food_selected_with_selected_ingredient.append(food_with_selected_ingredient)
                    chosen_ingredient.append(selected_ingredient)

    final_sorted_food_choose, suggested_ingredients = utils.indirect_search(food_selected_with_selected_ingredient,
                                                                            chosen_ingredient)
    user = request.user
    food_like_user, favorite_user = utils.get_info_user(user)
    context = {
        'previousIngredients': previous_ingredients,
        'previousFilter': {"cuisine": cuisine, "mealType": meal_type, "diet": diet, "site": site},
        'filterTypes_form': filter_types_form,
        'ingredients_form': ingredients_form,
        'finalSortedFoodChoose': final_sorted_food_choose,
        'suggested_ingredients': suggested_ingredients,
        'foodNames': [food.name for food in list(Food.objects.all())],
        'match_foods': match,
        'food_likes': food_like_user,
        'favorites': favorite_user,
    }
    return render(request, 'blog/search.html', context)


@login_required
def like(request):
    food_id = str(request.GET.get('foods'))
    food_selected = Food.objects.filter(id=food_id)
    index_selected = int(request.GET.get('index_selected'))
    if len(food_selected) == 0 or 5 < index_selected < 0:
        response = JsonResponse({"error": "there was an error"})
        response.status_code = 403
        return response
    food_selected = food_selected[0]
    last_score = 0
    id_current_user = request.user.id
    select_profile = list(Profile.objects.filter(user__id=id_current_user))[0]
    food_like_user = select_profile.food_likes.filter(food__id=food_id)
    print(food_id, food_like_user)
    sum_score_food = food_selected.number_of_score * food_selected.score
    if index_selected <= 5:
        if len(list(food_like_user)) == 0:
            food_selected.number_of_score += 1
            food_selected.save()
            food_like = FoodLike(food=food_selected, score=index_selected)
            food_like.save()
            select_profile.food_likes.add(food_like)
        else:
            last_score = list(food_like_user)[0].score
            food_like_user.update(score=index_selected)
        if index_selected == 1 and last_score > index_selected:
            new_score = -last_score
            food_like_user.update(score=0)
        else:
            new_score = index_selected - last_score

        # food_selected.score = round(FoodLike.objects.filter(food__name=food_like_user[0].food.name).aggregate(Avg('score'))['score__avg'] , 1)
        food_selected.score = (sum_score_food + new_score) / food_selected.number_of_score
        food_selected.save()
    return JsonResponse({'score': food_selected.score, 'number_of_score': food_selected.number_of_score})


@login_required
def update_profile(request):
    food_id = str(request.GET.get('foods'))
    food_selected = Food.objects.filter(id=food_id)
    if len(food_selected) == 0:
        response = JsonResponse({"error": "there was an error"})
        response.status_code = 403
        return response
    food_selected = food_selected[0]
    id_current_user = request.user.id
    select_profile = Profile.objects.get(user__id=id_current_user)
    user_favorite = list(select_profile.favorites.all())
    if food_selected not in user_favorite:
        select_profile.favorites.add(food_selected)
    else:
        select_profile.favorites.remove(food_selected)
    select_profile.save()
    return JsonResponse({})
