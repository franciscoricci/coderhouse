from django import forms
from .models import Persona, Deporte, Club


class Formulario(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["nombre", "fechadenacimiento"]
        labels = {'nombre': "Nombre", 'fechadenacimiento': "Fecha de Nacimiento"}

class Formulario_deporte(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = ["nombredeporte", "division"]
        labels = {'nombredeporte': "Nombre del deporte", 'division': "Division"}

class Formulario_club(forms.ModelForm):
    class Meta:
        model = Club
        fields = ["nombreclub", "pais"]
        labels = {'nombreclub': "Nombre del club", 'pais': "Pais"}
