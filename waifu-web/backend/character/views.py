from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from character.models import Character
from character.serializers import CharacterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes

@api_view(('GET', 'POST'))
@csrf_exempt
def character_all(request, format = None):
    if request.method == "GET":
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        serializer = CharacterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET', 'PUT', 'DELETE'))
@csrf_exempt
def character_single(request, pk, format = None):
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        print(request.data)
        serializer = CharacterSerializer(character, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # character = Character.get_object(pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
