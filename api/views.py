from django.shortcuts import render
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import exceptions

# Create your views here.
@api_view(['GET', 'POST'])
def drink_list(request : HttpRequest):
    if request.method == "GET":
        drinks = Drink.objects.all();
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])    
def drink_detail(request : HttpRequest, pk):
    try: 
        drink = Drink.objects.get(id = pk)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = DrinkSerializer(drink, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

