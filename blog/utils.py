from users.models import Profile
from .forms import ChooseIngredientsForm
from .models import Ingredient
from .models import Food


def direct_search(selected_food):
    match = []
    for _ in Food.objects.all():
        if len(selected_food) != 0:
            match = Food.objects.filter(name__icontains=selected_food)
        else:
            match = []
    return match


def update_ingredients_form():
    ChooseIngredientsForm.DAIRY = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="dairy")))
    ChooseIngredientsForm.BACKING_AND_GRAINS = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="backing_and_grains")))
    ChooseIngredientsForm.SWEETENERS = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="sweeteners")))
    ChooseIngredientsForm.VEGETABLES = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="vegetables")))
    ChooseIngredientsForm.FRUITS = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="fruits")))
    ChooseIngredientsForm.SPICES = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="spices")))
    ChooseIngredientsForm.MEATS = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="meats")))
    ChooseIngredientsForm.FISH_AND_SEAFOOD = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="fish_and_seafood")))
    ChooseIngredientsForm.CONDIMENTS = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="condiments")))
    ChooseIngredientsForm.BEVERAGES = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="beverages")))
    ChooseIngredientsForm.NUTS = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="nuts")))
    ChooseIngredientsForm.OIL = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="oil")))
    ChooseIngredientsForm.LEGUMES = tuple(
        ((item.name, item.name) for item in Ingredient.objects.filter(category="legumes")))
    ChooseIngredientsForm.SAUCES = tuple(
        (item.name, item.name) for item in Ingredient.objects.filter(category="sauces"))


def indirect_search(food_selected_with_selected_ingredient, chosen_ingredient):
    suggested_ingredients = []
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
                if name_food.name not in suggested_ingredients:
                    suggested_ingredients.append(name_food.name)
            final_sorted_food_choose[x] = unavailable_ingredients_str
    if len(suggested_ingredients) > 10:
        suggested_ingredients = suggested_ingredients[:10]
    return final_sorted_food_choose, suggested_ingredients


def get_info_user(user):
    filtered_users = Profile.objects.filter(user__username=user)
    if len(list(filtered_users)) != 0:
        dict_food_likes = {}
        select_profile = filtered_users[0]
        for food_liked in list(select_profile.food_likes.all()):
            dict_food_likes[food_liked.food.name] = food_liked.score
        return dict_food_likes, list(select_profile.favorites.all())
    return None , None
