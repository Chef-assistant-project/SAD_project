from django.db import models
from django.utils import timezone
from .forms import ChooseIngredientsForm, DIET, MEAL_TYPE, CUISINE ,FilterTypesForm

CATEGORY = (("dairy", "dairy"),
            ("vegetables", "vegetables"),
            ("fruits", "fruits"),
            ("backing_and_grains", "backing and grains"),
            ("sweeteners", "sweeteners"),
            ("spices", "spices"),
            ("meats", "meats"),
            ("fish_and_seafood", "fish and seafood"),
            ("condiments", "condiments"),
            ("beverages", "beverages"),
            ("nuts", "nuts"),
            ("oil", "oil"),
            ("sauces", "sauces"),
            ("legumes", "legumes")
            )


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True ,help_text="Must be a unique name.")
    category = models.CharField(choices=CATEGORY, default="", max_length=100)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Ingredient, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        ChooseIngredientsForm.DAIRY = tuple(
            ((item.name, item.name) for item in Ingredient.objects.filter(category="dairy")))
        ChooseIngredientsForm.BACKING_AND_GRAINS = tuple(
            ((item.name, item.name) for item in Ingredient.objects.filter(category="backing_and_rains")))
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


class Food(models.Model):
    name = models.CharField(max_length=100,
                            unique=True,
                            help_text="Must be a unique name."
                            )
    mealType = models.CharField(choices=MEAL_TYPE, default="", max_length=100)
    cuisine = models.CharField(choices=CUISINE, default="", max_length=100)
    diet = models.CharField(choices=DIET, default="", max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    date_added = models.DateTimeField(auto_now_add=True,editable=False)
    url = models.URLField(max_length=200)
    score = models.FloatField(default=0)
    number_of_score = models.IntegerField(default=0)
    detail = models.CharField(max_length=1000)
    image = models.ImageField()

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Food, self).save(force_insert, force_update, using, update_fields)
        ChooseIngredientsForm.DAIRY = tuple(
            ((item.name, item.name) for item in Ingredient.objects.filter(category="dairy")))
        FilterTypesForm.SITE = {food.url.split('/')[2].replace("www.", "") for food in Food.objects.all()}
        FilterTypesForm.SITE = (("all","all"),)+tuple((item, item) for item in FilterTypesForm.SITE)

