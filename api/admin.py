""""codigo"""
from django.contrib import admin
from .models import Respuestaschatbot
from .models import Registros
from .models import RegistroInicioSesion
from .models import RegistroCierreSesion

# Register your models here.
admin.site.register(Registros)
admin.site.register(Respuestaschatbot)
admin.site.register(RegistroInicioSesion)
admin.site.register(RegistroCierreSesion)
