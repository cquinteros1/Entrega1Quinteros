from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from AppCreditos.models import *


# Create your views here.

#Pagina Inicio ---------------------------------------------------------------------------------------------------

def inicio(request):
    return render(request,"AppCreditos/inicio.html")



#Carga de Creditos -----------------------------------------------------------------------------------------------

def form_carga(request):
    
    if request.method == 'POST':
        cr = Creditos(nro_cred=request.POST["nro_cred"], #el nro_cred en celeste (izquierda) viene de models.py y el "nro_cred" en rosado (derecha) viene del <form> de creditos.html (name)
                     fecha=request.POST["fecha"],
                     importe=request.POST["importe"],
                     cuotas=request.POST["cuotas"])
        cr.save()
        
        cl = Cliente(nombre=request.POST["nombre"],
                     apellido=request.POST["apellido"],
                     dni=request.POST["dni"],
                     fecha_nac=request.POST["fecha_nac"])
        cl.save()
        
        cm = Comercio(nombre_com=request.POST["nombre_com"],
                      rubro=request.POST["rubro"])
        cm.save()
        
        return render(request,'AppCreditos/cargaok.html')
    
    return render(request, 'AppCreditos/creditos.html')



#Busqueda Cliente ----------------------------------------------------------------------------------------------

def busquedaCreditos(request):
    
    return render(request, 'AppCreditos/busquedaCreditos.html')



#Resultados Busqueda -------------------------------------------------------------------------------------------

def resultados(request):

    if request.GET["dni"]:

        dni=request.GET["dni"]

        cliente=Cliente.objects.filter(dni__iexact=dni)

        return render(request, 'AppCreditos/resultados.html', {"Cliente":cliente, "dni":dni})
    
    else:

        #rta="No enviaste datos"
        return render(request, 'AppCreditos/sindatos.html')

    #return HttpResponse(rta)
