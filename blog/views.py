from _operator import getitem

from django.shortcuts import render
from .models import Food, Ingredient
from .forms import ChooseIngredientsForm


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def search(request):
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
    food_selected_with_selected_ingredient = []
    chosenIngridient = []

    # ingredient search :
    if request.method == "POST":
        if ingredients_form.is_valid():
            for form in ingredients_form:
                if form.name in request.POST:
                    for selected_ingredient in request.POST.getlist(form.name):
                        food_with_selected_ingredient = Food.objects.filter(
                            ingredients__name__startswith=selected_ingredient)
                        food_selected_with_selected_ingredient.append(food_with_selected_ingredient)
                        chosenIngridient.append(selected_ingredient)

    chosenFood = {}
    for queryFood in food_selected_with_selected_ingredient:
        for food in queryFood:
            a = Ingredient.objects.filter(food__name__startswith = food.name)
            chosenFood.update({food: {"Ingridient": a, "list of unavailable ingridients": list(a)}})

    for x in chosenFood:
        tempListOfUnavailableIngridients = chosenFood[x]["list of unavailable ingridients"].copy()
        for ingredient in chosenIngridient:
            for chosenfood in chosenFood.get(x).get("Ingridient"):
                if ingredient == chosenfood.name:
                    for unavailableIngridients in chosenFood[x]["list of unavailable ingridients"]:
                        if ingredient == unavailableIngridients.name:
                            tempListOfUnavailableIngridients.remove(unavailableIngridients)
                    chosenFood[x] = {"Ingridient": chosenFood.get(x).get("Ingridient"),
                                     "list of unavailable ingridients": list(tempListOfUnavailableIngridients)}

    sortedChosenFood = dict(sorted(chosenFood.items(), key=lambda x: getitem(x[1], "list of unavailable ingridients")))
    finalSortedFoodChoose = {}
    for x in sortedChosenFood:
        if len(sortedChosenFood[x]["list of unavailable ingridients"]) == 0:
            finalSortedFoodChoose[x] = "You've got all the ingredients!"
        else:
            UnavailableIngridientsStr = "YOU MISS : "
            for nameFood in sortedChosenFood[x]["list of unavailable ingridients"]:
                UnavailableIngridientsStr += nameFood.name
            finalSortedFoodChoose[x] = UnavailableIngridientsStr
    allFoods = [food.name for food in list(Food.objects.all())]
    context = {
        'matchFoods': match,
        'ingredients_form': ingredients_form,
        'foodNames': allFoods,
        'finalSortedFoodChoose': finalSortedFoodChoose
    }
    return render(request, 'blog/search.html', context)
