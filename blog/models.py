from django.db import models
from django.utils import timezone
from .forms import ChooseIngredientsForm


DIET = (
    ("vegetarian", "vegetarian"),
    ("gluten free", "gluten free"),
    ("pescatarian", "pescatarian"),
    ("none", "")
)
CUISINE = (
    ("asian", "asian"),
    ("italian", "italian"),
    ("chinese", "chinese"),
    ("none", "")
)
MEAL_TYPE = (
    ("breakfast", "breakfast"),
    ("desserts", "desserts"),
    ("dinner", "dinner"),
    ("salads", "salads"),
    ("cakes", "cakes"),
    ("none", "")
)

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
            ("legumes", "legumes")
            )


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY, default="", max_length=100)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Ingredient,self).save(force_insert=False, force_update=False, using=None,update_fields=None)
        ChooseIngredientsForm.DAIRY = ((item.name, item.name) for item in Ingredient.objects.filter(category="dairy"))
        ChooseIngredientsForm.BACKING_AND_GRAINS = ((item.name, item.name) for item in
                                   Ingredient.objects.filter(category="backing_and_rains"))
        ChooseIngredientsForm.SWEETENERS = ((item.name, item.name) for item in Ingredient.objects.filter(category="sweeteners"))
        ChooseIngredientsForm.VEGETABLES = ((item.name, item.name) for item in Ingredient.objects.filter(category="vegetables"))
        ChooseIngredientsForm.FRUITS = ((item.name, item.name) for item in Ingredient.objects.filter(category="fruits"))
        ChooseIngredientsForm.SPICES = ((item.name, item.name) for item in Ingredient.objects.filter(category="spices"))
        ChooseIngredientsForm.MEATS = ((item.name, item.name) for item in Ingredient.objects.filter(category="meats"))
        ChooseIngredientsForm.FISH_AND_SEAFOOD = ((item.name, item.name) for item in Ingredient.objects.filter(category="fish_and_seafood"))
        ChooseIngredientsForm.CONDIMENTS = ((item.name, item.name) for item in Ingredient.objects.filter(category="condiments"))
        ChooseIngredientsForm.BEVERAGES = ((item.name, item.name) for item in Ingredient.objects.filter(category="beverages"))
        ChooseIngredientsForm.NUTS = ((item.name, item.name) for item in Ingredient.objects.filter(category="nuts"))
        ChooseIngredientsForm.OIL = ((item.name, item.name) for item in Ingredient.objects.filter(category="oil"))
        ChooseIngredientsForm.LEGUMES = ((item.name, item.name) for item in Ingredient.objects.filter(category="legumes"))

class Food(models.Model):
    name = models.CharField(max_length=100)
    mealType = models.CharField(choices=MEAL_TYPE, default="", max_length=100)
    cuisine = models.CharField(choices=CUISINE, default="", max_length=100)
    diet = models.CharField(choices=DIET, default="", max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    date_added = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=200)
    score = models.IntegerField(default=0)
    detail = models.CharField(max_length=1000)
    image = models.ImageField()

    def __str__(self):
        return self.name
