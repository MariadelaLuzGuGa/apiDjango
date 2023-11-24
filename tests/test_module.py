from django.test import TestCase
from api.models import Registros, RegistroInicioSesion, RegistroCierreSesion, Respuestaschatbot

class ModuloTestCase(TestCase):
    
    def test_registro_usuario(self):
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        self.assertTrue(Registros.objects.filter(uname="testuser").exists())

    def test_validacion_usuario(self):
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        session = RegistroInicioSesion.objects.create(usuario=user)
        self.assertTrue(RegistroInicioSesion.objects.filter(usuario=user).exists())

    def test_registro_preguntas(self):
        question = Respuestaschatbot.objects.create(nombre_completo="John Doe", pregunta1="Question 1", pregunta2="Question 2", pregunta3="Question 3", pregunta4="Question 4", pregunta5="Question 5", pregunta6="Question 6", pregunta7="Question 7")
        self.assertTrue(Respuestaschatbot.objects.filter(nombre_completo="John Doe").exists())

    def test_marca_tiempo_inicio_sesion(self):
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        session = RegistroInicioSesion.objects.create(usuario=user)
        self.assertTrue(RegistroInicioSesion.objects.filter(usuario=user, marca_tiempo=session.marca_tiempo).exists())

    def test_marca_tiempo_cierre_sesion(self):
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        session = RegistroCierreSesion.objects.create(usuario=user)
        self.assertTrue(RegistroCierreSesion.objects.filter(usuario=user, marca_tiempo=session.marca_tiempo).exists())

    def test_relacion_clave_externa_inicio_sesion(self):
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        session = RegistroInicioSesion.objects.create(usuario=user)
        self.assertEqual(session.usuario, user)
