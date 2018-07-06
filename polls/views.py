from django.shortcuts import render
from django.http import HttpResponse

# Comentario de teste.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
