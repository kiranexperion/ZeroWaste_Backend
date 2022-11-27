from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import wasteSerializer
from .models import wastes

@api_view(['GET'])
def getWastes(request):
    wasteList = wastes.objects.all()
    serializer = wasteSerializer(wasteList, many = True)
    return Response(serializer.data)