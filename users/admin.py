from django.contrib import admin

# Register your models here.
from users.models import Profile,Food_likes

admin.site.register(Profile)
admin.site.register(Food_likes)




