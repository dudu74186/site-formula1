from django.urls import path
from . import views
from f1_races.views import sessionsListView, DriversListView

urlpatterns = [
    path('redirecionamento/', views.redirecionamento, name='redirecionamento'),
    #path('sessions/', sessionsListView.as_view(), name ='sessions_list'),
    path('', DriversListView.as_view(), name='home'),
]
