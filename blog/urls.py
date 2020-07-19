from django.urls import path
from . import views , utils

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('search/', views.search, name='search-page'),
    path('like/', views.like, name='like-page'),
    path('updateProfile/', utils.UpdateProfile, name='update-profile-page'),

]
