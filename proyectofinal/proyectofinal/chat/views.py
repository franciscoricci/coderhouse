from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.template import loader

from .forms import MessageForm
from .models import ChatMessage


# Create your views here.
def send_msg(request):
    if request.method == "POST":
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            instance = message_form.save(commit=False)
            instance.sender = request.user
            instance.save()
            # post_form.save()
            messages.success(request, "Se ha enviado el mensaje!." )
            return redirect('homepage')
        else:
            messages.error(request, "No se ha podido enviar el mensaje.")
    else:
        message_form = MessageForm()
    return render(request, 'send_message.html', {'message_form': message_form})


def ver_mensajes(request):
    msgs = ChatMessage.objects.filter(receiver=request.user)
    template = loader.get_template('messages.html')
    context = {
        'msgs': msgs,
    }
    return HttpResponse(template.render(context, request))