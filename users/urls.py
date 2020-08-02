from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('changePassword/', views.ChangePassword.as_view(), name='changePassword'),
    path('changeEmail/', views.ChangeEmail.as_view(), name='changeEmail'),
    path('removeFromProfile/', views.remove_from_profile, name='remove_from_profile-page'),
]
