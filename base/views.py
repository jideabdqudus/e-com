from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def getRoutes(request):
  """Gets the routes for the API"""
  return JsonResponse('Hello', safe=False)
  