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
        for food in Food.objects.all():
            if len(selected_food) != 0:
                match = Food.objects.filter(name__icontains=selected_food)
            else:
                match = []
    Food_filter = []
    chooseIngridient = []
    # ingredient search :
    if request.method == "POST":
        if ingredients_form.is_valid():
            for form in ingredients_form:
                if form.name in request.POST:
                    print(request.POST.getlist(form.name))
                    for x in request.POST.getlist(form.name):
                        a = Food.objects.filter(ingredients__name__startswith=x)
                        Food_filter.append(a)
                        chooseIngridient.append(x)
    FoodChoose = {}
    for QueryFood in Food_filter:
        for y in QueryFood:
            a = Ingredient.objects.filter(food__name__startswith=y.name)
            FoodChoose.update({y: {"Ingridient": a, "have": 0, "donthave": a.count()}})

    for x in FoodChoose:
        for y in chooseIngridient:
            for i in FoodChoose.get(x).get("Ingridient"):
                if y == i.name:
                    c = FoodChoose.get(x).get("have") + 1
                    d = FoodChoose.get(x).get("donthave") - 1
                    FoodChoose.update({x: {"Ingridient": FoodChoose.get(x).get("Ingridient"), "have": c, "donthave": d}})
    print("FoodChoose1", FoodChoose)
    sorted_FoodChoose = sorted(FoodChoose.items(), key=lambda x: getitem(x[1], "donthave"))
    print("sorted_FoodChoose",sorted_FoodChoose)

    allFoods = [food.name for food in list(Food.objects.all())]
    context = {
        'matchFoods': match,
        'ingredients_form': ingredients_form,
        'foodNames': allFoods
    }
    return render(request, 'blog/search.html', context)
