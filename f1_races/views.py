# f1_races/views.py

from operator import index
from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import RequestConfig
from datetime import date

# Criar context para renderizar a classificação dos pilotos
def redirecionamento(request):
    return render(request, 'redir/home.html')

def home(request):
    return render(request, 'home/base.html')

