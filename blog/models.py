from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.title


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


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    mealType = models.CharField(choices=MEAL_TYPE, default="", max_length=100)
    cuisine = models.CharField(choices=CUISINE, default="", max_length=100)
    diet = models.CharField(choices=DIET, default="", max_length=100)

    ingredients = models.ManyToManyField(Ingredient)
    date_added = models.DateTimeField(default=timezone.now)
    url = models.URLField(max_length=200, default="https://www.google.com/")
    score = models.IntegerField(default=0)

    def _str_(self):
        return self.name