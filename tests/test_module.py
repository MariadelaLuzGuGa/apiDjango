from django.test import TestCase
from django.utils import timezone
from api.models import Registros, RegistroInicioSesion, RegistroCierreSesion, Respuestaschatbot
from django.db.utils import IntegrityError

class ModuloTestCase(TestCase):
            
    def test_registro_usuario(self):
        # Verifica que el usuario se registre correctamente
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        self.assertTrue(Registros.objects.filter(uname="testuser").exists())

    def test_validacion_usuario(self):
        # Verifica que la validación de usuario funcione correctamente
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        session = RegistroInicioSesion.objects.create(usuario=user)
        self.assertTrue(RegistroInicioSesion.objects.filter(usuario=user).exists())

    def test_password_igual(self):
        # Verifica que las contraseñas sean iguales
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="234567U", pass2="234567U")
        self.assertEqual(user.pass1, user.pass2)
    
    def test_creacion_varios_usuarios(self):
        # Crear varios usuarios que no repitan otra vez el mismo usuario en otro registro
        Registros.objects.create(uname='Martina$#!', email='1234@gmail.com', pass1='plmk', pass2='plmk')
        Registros.objects.create(uname='Martina2$#!', email='1234@gmail.com', pass1='123456789', pass2='123456789' )

        # Verificar que la cantidad de usuarios es correcta
        assert Registros.objects.count() == 2

   
    def test_registro_preguntas(self):
        #Verifica el registro de las repuestas en la encuesta del Sitio web
        question = Respuestaschatbot.objects.create(
            marca_temporal=timezone.now(),
            nombre_completo="John Doe", 
            pregunta1="Question 1", 
            pregunta2="Question 2", 
            pregunta3="Question 3", 
            pregunta4="Question 4", 
            pregunta5="Question 5", 
            pregunta6="Question 6", 
            pregunta7="Question 7"
        )
        self.assertTrue(Respuestaschatbot.objects.filter(nombre_completo="John Doe").exists())

    def test_marca_tiempo_inicio_sesion(self):
        #Registro de inicio de sesion en de usuario
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        session = RegistroInicioSesion.objects.create(usuario=user)
        self.assertTrue(RegistroInicioSesion.objects.filter(usuario=user, marca_tiempo=session.marca_tiempo).exists())

    def test_marca_tiempo_cierre_sesion(self):
        #Registro de inicio de cierre en de usuario
        user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
        session = RegistroCierreSesion.objects.create(usuario=user)
        self.assertTrue(RegistroCierreSesion.objects.filter(usuario=user, marca_tiempo=session.marca_tiempo).exists())

    # def test_relacion_clave_externa_inicio_sesion(self):
    #     user = Registros.objects.create(uname="testuser", email="test@example.com", pass1="password1", pass2="password1")
    #     session = RegistroInicioSesion.objects.create(usuario=user)
    #     self.assertEqual(session.usuario, user)