from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('', views.index, name='users_index'),
    path('profile', views.profile, name='user_profile'),
    path('api/v1/confirm_discord', views.confirm_discord, name='confirm_discord')
]