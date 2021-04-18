from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ("name", "gender", "age", "username", "email", "password", "created_at")