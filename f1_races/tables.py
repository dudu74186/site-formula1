import django_tables2 as tables
from .models import sessions,driver

class SessionsTable(tables.Table):
    class Meta:
        model = sessions
        template_name = 'django_tables2/bootstrap5.html' 
        attrs = {"class": "table table-dark"} # Adicionando classes do Bootstrap

class DriversTable(tables.Table):
    broadcast_name = tables.Column(verbose_name='Piloto')
    driver_number = tables.Column(verbose_name='N°')

    headshot_url = tables.TemplateColumn(template_name='home/image_link.html', 
                                         verbose_name='',
                                         orderable=False)

    class Meta:
        model = driver
        template_name = 'django_tables2/bootstrap5.html' 
        attrs = {"class": "table table-dark"} # Adicionando classes do Bootstrap
        fields = ('broadcast_name', 'driver_number') 