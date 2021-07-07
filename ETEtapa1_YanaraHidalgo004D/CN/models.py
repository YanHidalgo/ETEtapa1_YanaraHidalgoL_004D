from django.db import models

# Create your models here.
class Colaborador(models.Model):

    rutColaborador = models.IntegerField(primary_key=True, verbose_name="Rut del Colaborador")
    imgColaborador = models.ImageField(upload_to='colaborador/', verbose_name='Imagen/Logo del Colaborador')
    nombreColaborador = models.CharField(max_length=150, verbose_name='Nombre del Colaborador')
    telefColaborador = models.IntegerField(verbose_name='Telefono del Colaborador')
    direccionColaborador = models.CharField(max_length=250, verbose_name='Dirección del Colaborador')
    emailColaborador = models.CharField(max_length=100, verbose_name='Email del Colaborador')
    paisColaborador = models.CharField(max_length=100, verbose_name='Pais del Colaborador')
    contraseñaColaborador = models.CharField(max_length=8, verbose_name='Contraseña Colaborador')

    def __str__(self):
        return str(self.rutColaborador)