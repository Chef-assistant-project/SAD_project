from _operator import getitem

from django.shortcuts import render
from .models import Food, Ingredient
from .forms import ChooseIngredientsForm, FilterTypesForm

FoodChoose = []



def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    filterTypes_form = FilterTypesForm(request.POST or None)
    ingredients_form = ChooseIngredientsForm(request.POST or None)
    match = []
    # direct_search :
    if request.method == "POST":
        selected_food = str(request.POST.get('title') or "").strip()
        for _ in Food.objects.all():
            if len(selected_food) != 0:
                match = Food.objects.filter(name__icontains=selected_food)
            else:
                match = []

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
    chosenIngredient = []
    if request.method == "POST" and ingredients_form.is_valid():
        for form in ingredients_form:
            if form.name in request.POST:
                for selected_ingredient in request.POST.getlist(form.name):
                    food_with_selected_ingredient = Food.objects.filter(
                        ingredients__name__startswith=selected_ingredient)
                    if diet != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(diet=diet)
                    if cuisine != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(cuisine=cuisine)
                    if mealType != "all":
                        food_with_selected_ingredient = food_with_selected_ingredient.filter(mealType=mealType)
                    food_selected_with_selected_ingredient.append(food_with_selected_ingredient)
                    chosenIngredient.append(selected_ingredient)

    chosenFood = {}
    for queryFood in food_selected_with_selected_ingredient:
        for food in queryFood:
            a = Ingredient.objects.filter(food__name__startswith=food.name)
            chosenFood.update({food: {"Ingredients": a, "list of unavailable ingredients": list(a)}})
    for x in chosenFood:
        tempListOfUnavailableIngredients = chosenFood[x]["list of unavailable ingredients"].copy()
        for ingredient in chosenIngredient:
            for chosenfood in chosenFood.get(x).get("Ingredients"):
                if ingredient == chosenfood.name:
                    for unavailableIngredients in chosenFood[x]["list of unavailable ingredients"]:
                        if ingredient == unavailableIngredients.name:
                            tempListOfUnavailableIngredients.remove(unavailableIngredients)
                    chosenFood[x] = {"Ingredients": chosenFood.get(x).get("Ingredients"),
                                     "list of unavailable ingredients": list(tempListOfUnavailableIngredients)}

    sortedChosenFood = dict(sorted(chosenFood.items(), key=lambda x: len(x[1])))
    finalSortedFoodChoose = {}
    for x in sortedChosenFood:
        if len(sortedChosenFood[x]["list of unavailable ingredients"]) == 0:
            finalSortedFoodChoose[x] = "You've got all the ingredients!"
        else:
            UnavailableIngredientsStr = "YOU MISS : "
            for nameFood in sortedChosenFood[x]["list of unavailable ingredients"]:
                UnavailableIngredientsStr += nameFood.name
            finalSortedFoodChoose[x] = UnavailableIngredientsStr
    allFoods = [food.name for food in list(Food.objects.all())]
    if match:
        match = score(request, match)
    else:
        finalSortedFoodChoose = score(request, finalSortedFoodChoose)
    context = {
        'previousFilter': {"cuisine": cuisine, "mealType": mealType, "diet": diet},
        'filterTypes_form': filterTypes_form,
        'matchFoods': match,
        'ingredients_form': ingredients_form,
        'foodNames': allFoods,
        'finalSortedFoodChoose': finalSortedFoodChoose
    }
    return render(request, 'blog/search.html', context)


def score(request, FoodLists):
    global FoodChoose
    name = str(request.GET.get('foods'))
    action = str(request.GET.get('action'))
    if list(FoodLists):
        FoodChoose = FoodLists
    if name != "":
        if action == 'add':
            for food in FoodChoose:
                if food.name == name:
                    food.score += 1
                    food.save()

        elif action == 'minus':
            for food in FoodChoose:
                if food.name == name:
                    food.score -= 1
                    food.save()

    return FoodChoose
