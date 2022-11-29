from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ChatMessage



class MessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ["content", "receiver"]
        labels = {'content': "Contenido", 'receiver': "A quien desea enviar el mensaje?"}
