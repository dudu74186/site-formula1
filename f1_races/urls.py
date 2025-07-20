from django.urls import path
from . import views
from f1_races.views import sessionsListView

urlpatterns = [
    path('redirecionamento/', views.redirecionamento, name='redirecionamento'),
    path('', sessionsListView.as_view(template_name='home/base.html'), name='home'),
]
