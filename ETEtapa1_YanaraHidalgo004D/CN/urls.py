from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('administracion', views.administracion, name="administracion"),
    path('form', views.form, name = 'form'),
    path('form_modificar/<id>', views.form_modificar, name='form_modificar'),
    path('eliminar/<id>', views.eliminar, name = 'eliminar'),
]