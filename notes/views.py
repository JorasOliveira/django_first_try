from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

# Create your views here.
