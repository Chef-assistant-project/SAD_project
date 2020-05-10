from django.contrib import admin
from .models import Post, Ingredient, Food

admin.site.register(Post)
admin.site.register(Ingredient)
admin.site.register(Food)