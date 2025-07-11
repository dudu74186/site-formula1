from operator import index
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def redirecionamento(request):
    return render(request, 'redir/home.html')

def home(request):
    return render(request, 'home/base.html')
