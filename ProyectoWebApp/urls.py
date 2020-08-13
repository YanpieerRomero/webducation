from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('cursos/', views.cursos, name="Cursos"),
    path('blog/', views.blog, name="Blog"),
    path('juegos/', views.juegos, name="Juegos"),
]
