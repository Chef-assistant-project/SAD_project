from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from users.models import Profile, FoodLike
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
