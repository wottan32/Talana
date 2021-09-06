from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ClUserData
from .serializers import ClUserDataSerializer
from random import randint
from django.shortcuts import render


def SaveUser(request):
    return render(request, 'pages/SaveUser.html')


@api_view(['POST'])
def SaveUser(request):
    if request.method == "POST":
        SaveSerializer = ClUserDataSerializer(data=request.data)
        if SaveSerializer.is_valid():
            SaveSerializer.save()
            return Response(SaveSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(SaveSerializer.data, status=status.HTTP_400_BAD_REQUEST)


def random_rut(request):
    i = randint(0, ClUserData.objects.count() - 1)
    rut = ClUserData.objects.all()[i]  # obtener un rut al azar
