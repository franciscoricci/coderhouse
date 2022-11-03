from django.http import HttpResponse
from .models import Persona, Deporte, Club
from django.template import loader
from .forms import Formulario, Formulario_club, Formulario_deporte
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q


# def index(request):
#     context = {
#         'leyenda': "Este es el Home"
#     }
#     template = loader.get_template('polls/home.html')
#     return HttpResponse(template.render(context, request))

def ver_persona(request):
    persona_list = Persona.objects.all()
    template = loader.get_template('polls/persona.html')
    context = {
        'persona_list': persona_list,
    }
    return HttpResponse(template.render(context, request))

def ver_deporte(request):
    deporte_list = Deporte.objects.all()
    template = loader.get_template('polls/deporte.html')
    context = {
        'deporte_list': deporte_list,
    }
    return HttpResponse(template.render(context, request))

def ver_club(request):
    club_list = Club.objects.all()
    template = loader.get_template('polls/club.html')
    context = {
        'club_list': club_list,
    }
    return HttpResponse(template.render(context, request))

def mostrarformulario(request):
    if request.method == "POST":
        form = Formulario(request.POST)
        form1 = Formulario_deporte(request.POST)
        form2 = Formulario_club(request.POST)
        if form.is_valid():
            form.save()
            form1.save()
            form2.save()
    else:
        form = Formulario()
        form1 = Formulario_deporte(request.POST)
        form2 = Formulario_club(request.POST)
    return render(request, 'polls/home.html', {'form': form, 'form1': form1, 'form2': form2})

# def buscar_persona(request):
#     return render(request, "polls/buscar_persona.html")

def buscar(request):
    
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        persona_list = Persona.objects.filter(nombre__icontains=nombre)
        return render(request, "polls/results_persona.html", {"persona_list": persona_list, "nombre":nombre})

    else:
        respuesta = "No enviaste datos"

    return render(request, "polls/results.html", {"respuesta": respuesta})

# def buscar_deporte(request):
#     return render(request, "polls/buscar_deporte.html")

def buscard(request):
    
    if request.GET['nombredeporte']:
        nombre = request.GET['nombredeporte']
        deporte_list = Deporte.objects.filter(nombredeporte__icontains=nombre)
        return render(request, "polls/results_deporte.html", {"deporte_list": deporte_list, "nombredeporte":nombre})

    else:
        respuesta = "No enviaste datos"

    return render(request, "polls/results_deporte.html", {"respuesta": respuesta})

# def buscar_club(request):
#     return render(request, "polls/buscar_club.html")

def buscarc(request):
    
    if request.GET['nombreclub']:
        nombre = request.GET['nombreclub']
        club_list = Club.objects.filter(nombreclub__icontains=nombre)
        return render(request, "polls/results_club.html", {"club_list": club_list, "nombreclub":nombre})

    else:
        respuesta = "No enviaste datos"

    return render(request, "polls/results_club.html", {"respuesta": respuesta})