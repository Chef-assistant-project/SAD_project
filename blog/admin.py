from django.utils.html import format_html
from django.contrib import admin
from .models import Ingredient, Food


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Ingredient, IngredientAdmin)


class FoodAdmin(admin.ModelAdmin):
    readonly_fields = ("date_added",)
    list_display = ('image_tag', 'name', 'get_ingredients', 'score')

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:80px;height:70px;"/>'.format(obj.image.url))

    def get_ingredients(self, obj):
        return " / ".join([ingredient.name for ingredient in obj.ingredients.all()])

    get_ingredients.short_description = 'Ingredients'
    image_tag.short_description = 'Image'


admin.site.register(Food, FoodAdmin)

