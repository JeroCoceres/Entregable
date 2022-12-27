from django.shortcuts import render
from django.http import HttpResponse

from Familiares.models import lista_de_familiares

#def lista_de_familiares(request):

def crear_familiar(request):
    new_member = lista_de_familiares.objects.create(name= "Lucas", age = 4 , vaccine = True)
    print(new_member)
    return HttpResponse ("Nuevo familiar creado")


def lista_familiares(request):
    all_family = lista_de_familiares.objects.all()
    print(all_family)
    context = {
        "people": all_family,

    }
    return render (request, "template.html", context= context) 