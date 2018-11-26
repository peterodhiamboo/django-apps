from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
]
