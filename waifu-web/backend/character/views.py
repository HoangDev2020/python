from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from character.models import Character
from character.serializers import CharacterSerializer

def character_all(request):
    if request.method == "GET":
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "PUT":
        serializer = CharacterSerializer(characters, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)