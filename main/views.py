from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Test
from .serializers import TestSerializer

# Create your views here.

@api_view(['GET'])
def tests_list(request):
    if request.method == 'GET':
        data = Test.objects.all()
        serializer = TestSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)