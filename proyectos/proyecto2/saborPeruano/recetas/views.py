from django.shortcuts import render,redirect

from.models import Receta


# Create your views here.


def index(request):
    listaRecetas = Receta.objects.all()
    print(listaRecetas)
    
    return render(request,'index.html')

