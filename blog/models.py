from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Diet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MealType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#

class Food(models.Model):
    name = models.CharField(max_length=100)
    mealType = models.ForeignKey(MealType, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    date_added = models.DateTimeField(default=timezone.now)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    url = models.URLField(max_length=200 , default = "https://www.google.com/")
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name






