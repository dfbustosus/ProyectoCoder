from django.shortcuts import render
from AppCoder.models import Curso 
from django.http import HttpResponse
# Create your views here.
def curso(self):
    curso= Curso(nombre='Desarrollo Web', camada='19000')
    curso.save()
    documento= f'----> Curso: {curso.nombre}   Camada: {curso.camada}'
    return HttpResponse(documento)