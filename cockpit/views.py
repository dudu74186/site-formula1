from django.shortcuts import render
from django.http import HttpResponse

def pilotos(request):
    return render(request, 'piloto.html')

