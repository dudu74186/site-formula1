from django.urls import path
from . import views

urlpatterns = [
    path('Teste/', views.test_view, name='test_view')
]
