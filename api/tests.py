# from django.core.exceptions import ValidationError
# from django.test import TestCase
# from .models import Registros

# class RegistrosTestCase(TestCase):
#     def test_create_registro(self):
#         # Crea un registro válido
#         registro = Registros.objects.create(uname='usuario1', email='usuario1@example.com', pass1='clave123', pass2='clave123')

#         # Recupera el registro de la base de datos
#         registro_db = Registros.objects.get(uname='usuario1')

#         # Comprueba que los valores son correctos
#         self.assertEqual(registro_db.uname, 'usuario1')
#         self.assertEqual(registro_db.email, 'usuario1@example.com')
#         self.assertEqual(registro_db.pass1, 'clave123')
#         self.assertEqual(registro_db.pass2, 'clave123')


# from django.test import TestCase
# from api.models import Registros, Respuestaschatbot

# class RegistrosTest(TestCase):

#     def setUp(self):
#         # Configuración inicial, si es necesaria
#         self.registro = Registros.objects.create(uname='user123', email='usuario@example.com', pass1='clave123', pass2='clave123')

#     def tearDown(self):
#         # Limpiar las instancias creadas durante las pruebas
#         self.registro.delete()

#     def test_creacion_registro(self):
#         # Prueba para verificar la creación de un objeto Registros
#         self.assertEqual(Registros.objects.count(), 1, 'La creación de Registros falló')

#     def test_campos_registro(self):
#         # Prueba para verificar los campos del modelo Registros
#         self.assertEqual(self.registro.uname, 'user123')
#         self.assertEqual(self.registro.email, 'usuario@example.com')
#         self.assertEqual(self.registro.pass1, 'clave123')
#         self.assertEqual(self.registro.pass2, 'clave123')

# class RespuestaschatbotTest(TestCase):

#     def setUp(self):
#         # Configuración inicial, si es necesaria
#         self.respuesta = Respuestaschatbot.objects.create(
#             marca_temporal='2023-11-24 12:00:00',
#             nombre_completo='John Doe',
#             pregunta1='Respuesta1',
#             pregunta2='Respuesta2',
#             pregunta3='Respuesta3',
#             pregunta4='Respuesta4',
#             pregunta5='Respuesta5',
#             pregunta6='Respuesta6',
#             pregunta7='Respuesta7'
#         )

#     def tearDown(self):
#         # Limpiar las instancias creadas durante las pruebas
#         self.respuesta.delete()

#     def test_creacion_respuesta(self):
#         # Prueba para verificar la creación de un objeto Respuestaschatbot
#         self.assertEqual(Respuestaschatbot.objects.count(), 1, 'La creación de Respuestaschatbot falló')

#     def test_campos_respuesta(self):
#         # Prueba para verificar los campos del modelo Respuestaschatbot
#         self.assertEqual(str(self.respuesta.marca_temporal), '2023-11-24 12:00:00')
#         self.assertEqual(self.respuesta.nombre_completo, 'John Doe')
#         self.assertEqual(self.respuesta.pregunta1, 'Respuesta1')
#         self.assertEqual(self.respuesta.pregunta2, 'Respuesta2')
#         self.assertEqual(self.respuesta.pregunta3, 'Respuesta3')
#         self.assertEqual(self.respuesta.pregunta4, 'Respuesta4')
#         self.assertEqual(self.respuesta.pregunta5, 'Respuesta5')
#         self.assertEqual(self.respuesta.pregunta6, 'Respuesta6')
#         self.assertEqual(self.respuesta.pregunta7, 'Respuesta7')
