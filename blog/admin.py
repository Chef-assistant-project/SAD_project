from django.contrib import admin
from .models import Post 

from django.contrib import admin
from .models import Post, Ingredient, Food , MealType , Diet , Cuisine

admin.site.register(Post)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(Diet)
admin.site.register(MealType)
admin.site.register(Cuisine)
