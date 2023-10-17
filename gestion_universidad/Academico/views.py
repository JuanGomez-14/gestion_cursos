from django.shortcuts import redirect, render
from .models import Curso


def home(request):
    allCursos = Curso.objects.all()
    return render(request, 'gestionCursos.html', {"cursos": allCursos})


def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')
