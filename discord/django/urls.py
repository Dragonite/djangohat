from django.urls import path

from . import views

app_name = "bot-management"

urlpatterns = [
    path('', views.bot_landing, name='bot_landing'),
]