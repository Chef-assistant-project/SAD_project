from django.shortcuts import render
from .models import Food
from .forms import chooseIngredientsForm


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    ingredients_form = chooseIngredientsForm(request.POST or None)
    match = []

    # direct_search :
    if request.method == "POST":
        selected_food = str(request.POST.get('title') or "").strip()
        for food in Food.objects.all():
            if len(selected_food) != 0 :
                match = Food.objects.filter(name__icontains = selected_food)
            else:
                match = []

    # ingredient search :
    if request.method == "POST":
        if ingredients_form.is_valid():
            for form in ingredients_form:
                if form.name in request.POST:
                    print(request.POST.getlist(form.name))
            # return render(request, 'blog/search.html', context)
    context = {
        'matchFoods': match,
        'ingredients_form': ingredients_form
    }
    return render(request, 'blog/search.html', context)


