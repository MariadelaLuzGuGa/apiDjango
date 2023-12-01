"""
Codigo para La BASE DE DATOS de Registro y formulario de POSGRETSQL
"""
from django.db import models

# Create your models here.
class Registros(models.Model):
    """Metodo de REGISTRO de la Primera tabla"""
    uname = models.CharField(max_length=30, primary_key=True)
    email = models.EmailField()
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.uname, self.email)

class Respuestaschatbot(models.Model):
    marca_temporal = models.DateTimeField()
    nombre_completo = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=100)
    pregunta2 = models.TextField()
    pregunta3 = models.CharField(max_length=100)
    pregunta4 = models.TextField()
    pregunta5 = models.TextField()
    pregunta6 = models.CharField(max_length=100)
    pregunta7 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre_completo)
    



class RegistroInicioSesion(models.Model):
    usuario = models.ForeignKey('Registros', on_delete=models.CASCADE)
    marca_tiempo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.usuario)

class RegistroCierreSesion(models.Model):
    usuario = models.ForeignKey('Registros', on_delete=models.CASCADE)
    marca_tiempo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.usuario)