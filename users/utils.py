from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from users.models import Profile, FoodLike
from .models import Food


