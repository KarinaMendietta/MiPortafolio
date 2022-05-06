from django.shortcuts import render

from.models import Autor,Receta,Comentario


# Create your views here.


def index(request):
    listaRecetas = Receta.objects.all()
    context = {
        'recetas':listaRecetas
    }
    print(listaRecetas)
    
    return render(request,'index.html',context)

