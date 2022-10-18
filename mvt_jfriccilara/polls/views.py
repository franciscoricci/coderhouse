from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from django.template import loader

# Create your views here.
def index(request):
    persona_list = Persona.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'persona_list': persona_list,
    }
    return HttpResponse(template.render(context, request))

