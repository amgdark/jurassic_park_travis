
from django.urls import path
from . import views

urlpatterns = [
    path('',views.lista_periodo, name='lista_periodo'),
    path('agregar',views.agregar_periodo, name='agregar_periodo'),
    path('agregar/dino',views.agregar_dino, name='agregar_dino'),
    path('nuevo/dino',views.NuevoDino.as_view(), name='nuevo_dino'),
    path('dinos',views.ListaDino.as_view(), name='lista_dinos'),
    path('eliminar/<int:id>',views.eliminar_periodo, name='eliminar_periodo'),
    path('editar/<int:id>',views.editar_periodo, name='editar_periodo'),
]
