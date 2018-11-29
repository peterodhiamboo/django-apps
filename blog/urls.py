from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from user import views as user_views


urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('about/', views.about, name = 'aboutpage'),
    path('login/', views.user_login, name="login"),
    path('register', user_views.register, name='registration'),
    path('logout', views.user_logout, name='logout'),
    path('create_post/', views.create_new_post, name='new_post'),
    path('edit_post/<post_id>', views.edit_post, name='edit_post')
]
