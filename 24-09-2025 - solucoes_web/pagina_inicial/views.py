from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá! Bem-vindo à solução Web Rápidas! Em breve, um novo site para impulsionar o seu negócio.")
# Create your views here.