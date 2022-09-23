from django.urls import path
from AppCreditos.views import *

urlpatterns = [
    path('', inicio, name='INICIO'),
    path('creditos/', form_carga, name="CREDITOS"),
    path('buscarCreditos/', busquedaCreditos, name="BUSCAR"),
    path('resultados/', resultados, name="ResultadosBusqueda"),
]