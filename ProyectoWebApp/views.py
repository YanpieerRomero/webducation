from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "ProyectoWebApp/home.html")


def cursos(request):
    return render(request, "ProyectoWebApp/cursos.html")


def blog(request):
    return render(request, "ProyectoWebApp/blog.html")


def juegos(request):
    return render(request, "ProyectoWebApp/juegos.html")
