from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(blank=True, max_length=200)
    apellido = models.CharField(blank=True, max_length=200)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, null=True)
    
    

    def __str__(self):
        return self.nombre