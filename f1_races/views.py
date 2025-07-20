from operator import index
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import sessions

# Create your views here.
def redirecionamento(request):
    return render(request, 'redir/home.html')

def home(request):
    return render(request, 'home/base.html')

class sessionsListView(ListView):
    model = sessions
    template_name = 'home/base.html'
    
    