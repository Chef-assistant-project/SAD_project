from django.urls import path
from blog import views , utils

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('search/', views.search, name='search-page'),
    path('like/', views.like, name='like-page'),
    path('updateProfile/', utils.update_profile, name='update-profile-page'),

]
