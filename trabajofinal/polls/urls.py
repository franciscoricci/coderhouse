from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='Home'),
    path('', views.mostrarformulario, name='Home'),
    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    path('persona/', views.ver_persona, name='Personas'),
    # ex: /polls/5/results/
    path('deporte/', views.ver_deporte, name='Deportes'),
    # ex: /polls/5/vote/
    path('club/', views.ver_club, name='Clubs'),
    #<int:club_id>/
    path('formulario/', views.mostrarformulario, name='form'),
    #path('buscar_persona/', views.buscar_persona, name='form'),
    path('buscar/', views.buscar),
    #path('buscar_deporte/', views.buscar_deporte, name='form'),
    path('buscard/', views.buscard),
    #path('buscar_club/', views.buscar_club, name='form'),
    path('buscarc/', views.buscarc),
]
