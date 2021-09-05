from django.contrib import admin
from django.urls import path, include
# from escola.views import alunos
from escola.views import AlunosViewset, CursosViewset, MatriculaViewset, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewset, basename='Alunos')
router.register('cursos', CursosViewset, basename='Cursos')
router.register('matricula', MatriculaViewset, basename='Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matricula/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matricula/', ListaAlunosMatriculados.as_view())
    # path('alunos/', alunos),
]
