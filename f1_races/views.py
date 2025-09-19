# f1_races/views.py
from django.shortcuts import render
from .models import races_driver_standings
from django.db.models import Max

# Criar context para renderizar a classificação dos pilotos
def redirecionamento(request):
    return render(request, 'redir/home.html')

def home(request):
    maior_valor_da_coluna = races_driver_standings.objects.aggregate(Max('raceID'))
    
    pilots = races_driver_standings.objects.filter(raceID=maior_valor_da_coluna['raceID__max'])




    context = {
        'pilots': pilots,
    }


    return render(request, 'home/base.html', context)

