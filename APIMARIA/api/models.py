# """
# Codigo para La BASE DE DATOS de Servico Social del TESCHI
# """
# from django.db import models

# # Create your models here.
# class Registros(models.Model):
#     """Metodo de REGISTRO de la Primera tabla"""
#     uname = models.CharField(max_length=30, primary_key=True)
#     email = models.EmailField()
#     pass1 = models.CharField(max_length=50)
#     pass2 = models.CharField(max_length=50)

#     def __str__(self):
#         texto = "{0}({1})"
#         return texto.format(self.user, self.email)
