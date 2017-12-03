from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import animals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .searializer import AnimalsSerializer

# Create your views here.

def index():

    pass

class AnimalsList(APIView):

    """
    Lists all active companies
    """

    def get(self, request, format=None):
        # Get all objects from database
        company = animals.objects.all()
        # Pass all objects through to BusinessProfileSerializer class
        serializer = AnimalsSerializer(company, many=True)
        # Return JSON response
        return Response(serializer.data)