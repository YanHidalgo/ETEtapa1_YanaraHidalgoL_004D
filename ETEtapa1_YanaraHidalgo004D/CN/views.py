from django.shortcuts import render, redirect
from . import models
from .form import formColaborador

# Create your views here.
def index( request ):
    return render(request, 'CN/index.html')

def administracion( request ):
    colaborador = models.Colaborador.objects.all()
    datos = {
        'colaborador': colaborador
    }
    return render(request, 'CN/administracion.html', datos)

def form( request ):
    if request.method=='POST':
        form = formColaborador( request.POST, request.FILES  )
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('administracion')
    else:
        form = formColaborador()
        return render(request, 'CN/form.html', {'form': formColaborador})


def form_modificar(request, id):
    colaborador = models.Colaborador.objects.get(rutColaborador = id)
    datos = {
        'form': formColaborador(instance = colaborador)
    }
    if request.method =='POST':
        formulario = formColaborador(request.POST, request.FILES, instance=colaborador)
        if formulario.is_valid:
            colaborador = models.Colaborador.objects.get(rutColaborador = id)
            colaborador.delete()
            formulario.save()
            return redirect('index')
    return render(request, 'CN/form_modificar.html', datos)

def eliminar(request, id):
    colaborador = models.Colaborador.objects.get(rutColaborador = id)
    colaborador.delete()
    return redirect(to="administracion")