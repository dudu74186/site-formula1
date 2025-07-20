import django_tables2 as tables
from .models import sessions

class SessionsTable(tables.Table):
    class Meta:
        model = sessions
        template_name = 'home/base.html'