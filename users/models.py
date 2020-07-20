from django.db import models
from django.contrib.auth.models import User
from blog.models import Food


class FoodLike(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        template = '{0.name} {0.score}'
        return template.format(self)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    favorites = models.ManyToManyField(Food)
    food_likes = models.ManyToManyField(FoodLike)

    def __str__(self):
        return self.user.username
