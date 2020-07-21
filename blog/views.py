from django.http import JsonResponse
from django.shortcuts import render
from blog import utils
from .models import Food, Ingredient
from users.models import Profile
from .forms import ChooseIngredientsForm, FilterTypesForm


def home(request):
    best_food_score = Food.objects.order_by('-score')[:3]
    print("best_food_score", best_food_score)
    context = {
        'best_food_score': best_food_score,
        # 'best_foods1': best_food_score[0],
        # 'best_foods2': best_food_score[1],
        # 'best_foods3': best_food_score[2],

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
    if request.method == "POST" and filterTypes_form.is_valid():
        if "diet" in request.POST:
            diet = request.POST.get("diet")

        if "cuisine" in request.POST:
            cuisine = request.POST.get("cuisine")

        if "mealType" in request.POST:
            mealType = request.POST.get("mealType")

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

    ### sogand check it pls :)
    # sorted_chosen_food = dict(sorted(chosen_food.items(), key=lambda x: len(x[1])))
    sorted_chosen_food = dict(
        sorted(chosen_food.items(), key=lambda x: len(x[1].get("list of unavailable ingredients"))))
    print(sorted_chosen_food)
    print(sorted_chosen_food)
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
        'previousFilter': {"cuisine": cuisine, "mealType": mealType, "diet": diet},
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
            food, score = str(food_liked).split()
            dict_food_likes[food] = int(score)
        context['food_likes'] = dict_food_likes
        context['favorites'] = list(select_profile.favorites.all())

    return render(request, 'blog/search.html', context)


def like(request):
    return utils.Score(request)
