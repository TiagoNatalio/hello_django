from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos!</h1>'.format(nome,idade))

def somaValores(request,n1,n2):
    soma = n1 + n2
    return HttpResponse('<h2>A soma é {}</h2>'.format(soma))
    
def subtracaoValores(request,n1,n2):
    soma = n1 - n2
    return HttpResponse('<h2>A subtração é {}</h2>'.format(soma))

def divisaoValores(request,n1,n2):
    soma = n1 / n2
    return HttpResponse('<h2>A divisão é {}</h2>'.format(soma))

def multiplicacaoValores(request,n1,n2):
    soma = n1 * n2
    return HttpResponse('<h2>A multiplicação é {}</h2>'.format(soma))