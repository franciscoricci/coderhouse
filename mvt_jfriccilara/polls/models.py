from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    documento = models.BigIntegerField()
