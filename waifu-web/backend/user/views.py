from django.shortcuts import render
import bcrypt
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from user.models import User
from user.serializers import UserSerializer
from rest_framework import serializers
from django.core import serializers as core_serializers
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import jwt

SALT = b'$2b$12$KBEAegqlBZsxan0pulUSfu'

@api_view(['POST'])
@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        hashed = bcrypt.hashpw(data["password"].encode('utf-8'), SALT).decode("utf-8")
        data["password"] = hashed
        user = UserSerializer(data = data)
        if user.is_valid():
            user.save()
            return JsonResponse(user.data, status = 200)
        return JsonResponse(user.errors, status = 400)

@csrf_exempt
def sign_in(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        try:
            user = User.objects.filter(email = data["email"])[0]
        except:
            return JsonResponse({"message": "invalid email"}, status = 404)
        # serializers = UserSerializer(data = data)
        user = core_serializers.serialize('json', [user,])
        user = json.loads(user)[0]["fields"]
        hashed = bcrypt.hashpw(data["password"].encode('utf-8'), SALT).decode("utf-8")
        if user["password"] == hashed:
            encoded_jwt = jwt.encode({"email": user["email"]}, SECRET_KEY, algorithm = "HS256")
            return JsonResponse({"token": encoded_jwt.decode("utf-8")})
        return JsonResponse({"message": "invalid password"})