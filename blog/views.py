from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog import utils
from .models import Food, Ingredient
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
    match = []
    if request.method == "POST":
        match = utils.direct_search(str(request.POST.get('title') or "").strip())

    filterTypes_form = FilterTypesForm(request.POST or None)
    ingredients_form = ChooseIngredientsForm(request.POST or None)
    cuisine = "all"
    diet = "all"
    mealType = "all"
    site = "all"
    if request.method == "POST" and filterTypes_form.is_valid():
        if "diet" in request.POST:
            diet = request.POST.get("diet")

        if "cuisine" in request.POST:
            cuisine = request.POST.get("cuisine")

        if "mealType" in request.POST:
            mealType = request.POST.get("mealType")

        if "site" in request.POST:
            site = request.POST.get("site")

    # ingredient search :
    food_selected_with_selected_ingredient = []
    chosen_ingredient = []
    if request.method == "POST" and ingredients_form.is_valid():
        for form in ingredients_form:
            if form.name in request.POST:
                for selected_ingredient in request.POST.getlist(form.name):
                    food_with_selected_ingredient = Food.objects.filter(ingredients__name=selected_ingredient)
                    if diet != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(diet=diet)
                    if cuisine != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(cuisine=cuisine)
                    if mealType != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(mealType=mealType)
                    if site != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(url__icontains=site)
                    food_selected_with_selected_ingredient.append(food_with_selected_ingredient)
                    chosen_ingredient.append(selected_ingredient)

    chosen_food = {}
    for query_food in food_selected_with_selected_ingredient:
        for food in query_food:
            a = Ingredient.objects.filter(food__name=food.name)
            chosen_food.update({food: {"Ingredients": a, "list of unavailable ingredients": list(a)}})
    for x in chosen_food:
        temp_list_of_unavailable_ingredients = chosen_food[x]["list of unavailable ingredients"].copy()
        for ingredient in chosen_ingredient:
            for selected_food in chosen_food.get(x).get("Ingredients"):
                if ingredient == selected_food.name:
                    for unavailableIngredients in chosen_food[x]["list of unavailable ingredients"]:
                        if ingredient == unavailableIngredients.name:
                            temp_list_of_unavailable_ingredients.remove(unavailableIngredients)
                    chosen_food[x] = {"Ingredients": chosen_food.get(x).get("Ingredients"),
                                      "list of unavailable ingredients": list(temp_list_of_unavailable_ingredients)}

    sorted_chosen_food = dict(
        sorted(chosen_food.items(), key=lambda x: len(x[1].get("list of unavailable ingredients"))))
    final_sorted_food_choose = {}
    for x in sorted_chosen_food:
        if len(sorted_chosen_food[x]["list of unavailable ingredients"]) == 0:
            final_sorted_food_choose[x] = "You've got all the ingredients!"
        else:
            unavailable_ingredients_str = "YOU MISS : "
            for name_food in sorted_chosen_food[x]["list of unavailable ingredients"]:
                unavailable_ingredients_str += ' ' + name_food.name
            final_sorted_food_choose[x] = unavailable_ingredients_str

    all_foods = [food.name for food in list(Food.objects.all())]

    context = {
        'previousFilter': {"cuisine": cuisine, "mealType": mealType, "diet": diet ,"site" :site },
        'filterTypes_form': filterTypes_form,
        'ingredients_form': ingredients_form,
        'finalSortedFoodChoose': final_sorted_food_choose,
        'foodNames': all_foods,
        'match_foods': match,
    }
    user = request.user
    filtered_users = Profile.objects.filter(user__username=user)
    if len(list(filtered_users)) != 0:
        select_profile = filtered_users[0]
        dict_food_likes = {}
        for food_liked in list(select_profile.food_likes.all()):
            dict_food_likes[food_liked.food.name] = food_liked.score
        context['food_likes'] = dict_food_likes
        context['favorites'] = list(select_profile.favorites.all())

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

        food_selected.score = (sum_score_food + new_score) / food_selected.number_of_score
        food_selected.save()

    return JsonResponse({'likes': food_selected.score})


@login_required
def update_profile(request):
    food_id = str(request.GET.get('foods'))
    food_selected = Food.objects.filter(id=food_id)
    if len(food_selected) == 0:
        print("****")
        response = JsonResponse({"error": "there was an error"})
        response.status_code = 403
        return response
    food_selected=food_selected[0]
    id_current_user = request.user.id
    select_profile = Profile.objects.get(user__id=id_current_user)
    user_favorite = list(select_profile.favorites.all())
    if food_selected not in user_favorite:
        select_profile.favorites.add(food_selected)
    else:
        select_profile.favorites.remove(food_selected)
    select_profile.save()
    return JsonResponse({})
