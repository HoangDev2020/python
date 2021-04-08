from django.urls import path
from character import views

urlpatterns = [
    path("", views.character_all)
]