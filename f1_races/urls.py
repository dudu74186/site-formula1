from django.urls import path
from . import views

urlpatterns = [
    path('redirecionamento/', views.redirecionamento, name='redirecionamento'),
    path('', views.home, name='home'),
]
