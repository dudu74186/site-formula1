# f1_races/views.py

from operator import index
from django.shortcuts import render
from django.views.generic import ListView
from .models import sessions,driver
from .tables import SessionsTable, DriversTable
from django_tables2 import RequestConfig
from datetime import date

# Create your views here.
def redirecionamento(request):
    return render(request, 'redir/home.html')

def home(request):
    return render(request, 'home/base.html')

class sessionsListView(ListView):
    model = sessions
    template_name = 'home/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = SessionsTable(self.object_list)
        RequestConfig(self.request).configure(table)
        context['table'] = table
        return context

class DriversListView(ListView):
    model = driver
    template_name = 'home/base.html'

    def get_queryset(self):
        actual_year = date.today().year
        queryset = super().get_queryset()
        queryset = queryset.filter(sessions__year = actual_year)
        queryset = queryset.distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = DriversTable(self.object_list)
        RequestConfig(self.request).configure(table)
        context['table'] = table
        return context
