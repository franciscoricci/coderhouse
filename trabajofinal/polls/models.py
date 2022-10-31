from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fechadenacimiento = models.DateTimeField('Fecha de Nacimiento')
    def __str__(self):
        return self.nombre

class Deporte(models.Model):
    nombredeporte = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    def __str__(self):
        return self.nombredeporte

class Club(models.Model):
    nombreclub = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    def __str__(self):
        return self.nombreclub