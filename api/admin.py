""""codigo"""
from django.contrib import admin
from .models import Respuestaschatbot
from .models import Registros
# Register your models here.
admin.site.register(Registros)
admin.site.register(Respuestaschatbot)
