from django.urls import path
from user import views

urlpatterns = [
    path("sign_up", views.sign_up)
]
