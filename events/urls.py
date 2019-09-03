from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path('', views.index, name='event_index'),
    path('create/', views.create_event, name='create_event'),
]