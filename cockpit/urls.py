from django.urls import path
from . import views

urlpatterns = [
    path('pilotos/', views.pilotos, name="pilotos")
]