from django.urls import path
from character import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.character_all),
    path('<int:pk>', views.character_single)
]

urlpatterns = format_suffix_patterns(urlpatterns)