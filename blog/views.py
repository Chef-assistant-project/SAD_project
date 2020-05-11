from django.shortcuts import render
from .models import  Food
from .forms import chooseIngredientsForm

# ingredients = models.ManyToManyField(Ingredient)


food = [
    {
        'name': 'Soft-Boiled Eggs',
        'mealType': 'Breakfast',
        'cuisine': 'all',
        'diet': 'all',
        'url': 'https://www.marthastewart.com/318363/soft-boiled-eggs',
        'score': 0,
        'isFavorite': False,
        'date': '10 Jan 2018',
        'image': 'b2.jpg',
        'detail': 'Cooking Perfect Boiled Eggs in minutes'
    },
    {
        'name': 'Creamy Scrambled Eggs',
        'mealType': 'Breakfast',
        'cuisine': 'all',
        'diet': 'all',
        'url': 'https://food52.com/recipes/36211-lady-pups-s-magic-15-second-creamy-scrambled-eggs',
        'score': 0,
        'isFavorite': False,
        'date': '10 Jan 2018',
        'image': 'b5.jpg',
        'detail': 'Cooking Perfect Creamy Scrambled Eggs in minutes'

    },
    {
        'name': 'Thai green curry chicken',
        'mealType': 'Dinner',
        'cuisine': 'Asian',
        'diet': 'all',
        'url': 'https://www.chatelaine.com/recipe/world-cuisine-2/thai-green-curry-chicken/',
        'score': 0,
        'isFavorite': False,
        'date': '10 Jan 2018',
        'image': 'b7.jpg',
        'detail': 'Cooking Perfect Thai green curry chicken '
    }
]


def home(request):

    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    ingredients_form = chooseIngredientsForm(request.POST or None)
    match = []
    context = {
        'matchFoods': match,
        'ingredients_form': ingredients_form
    }

    # direct_search :
    selected_food = str(request.POST.get('title') or "")
    for i in range(len(food)):
        if len(selected_food) != 0 and selected_food.lower() in list(food[i].values())[0].lower():
            match.append(food[i])

    # ingredient search :
    if request.method == "POST":
        if ingredients_form.is_valid():
            for form in ingredients_form:
                if form.name in request.POST:
                    print(request.POST.getlist(form.name))
            return render(request, 'blog/search.html', context)

    return render(request, 'blog/search.html', context)



