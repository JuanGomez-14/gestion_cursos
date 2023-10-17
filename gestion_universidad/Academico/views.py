from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages


def home(request):
    allCursos = Curso.objects.all()
    return render(request, 'gestionCursos.html', {"cursos": allCursos})


def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    allCursos = Curso.objects.all()

    for curso1 in allCursos:
        print(curso1.codigo)
        if codigo == curso1.codigo:
            messages.warning(request, '¡El código ya está en uso!')
            return redirect('/')

    Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/')


def editarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'editarCurso.html', {'curso': curso})


def edicionCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso editado!')

    return redirect('/')
