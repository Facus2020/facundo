from operator import lt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

# Create your views here.
def persona_list(request):
    #return HttpResponse ('Soy el inicio')
    personas = Persona.objects.filter(sexo="F")
    persona1 = Persona.objects.filter(sexo="M")
    persona2 = Persona.objects.filter(edad__lt=18)
    persona3 = Persona.objects.filter(edad__gte=19)
    return render(request, 'amigachos/persona_list.html', {'personas': personas, 'persona1': persona1, 'persona2': persona2, 'persona3':persona3})
