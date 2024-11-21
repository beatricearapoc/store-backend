from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def products(request):
    if request.method == "GET":
          return Response({"message": "Hello World"})

