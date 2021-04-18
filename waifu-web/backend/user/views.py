from django.shortcuts import render
import bcrypt
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from user.models import User
from user.serializers import UserSerializer
from rest_framework.decorators import api_view


SALT = b'$2b$12$KBEAegqlBZsxan0pulUSfu'

@api_view(['POST'])
@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        hashed = bcrypt.hashpw(data["password"].encode('utf-8'), SALT)