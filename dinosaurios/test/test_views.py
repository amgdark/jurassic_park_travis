from django.test import TestCase
from dinosaurios.models import Dinosaurio, Periodo, VotacionDino
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_url_dinos_votacion(self):
        self.user_login()
        response = self.client.get('/periodo/dinos/votacion')
        self.assertEqual(response.status_code, 200)

    def test_redireccion_a_login_dinos_votacion(self):
        response = self.client.get('/periodo/dinos/votacion')
        self.assertRedirects(response, '/usuarios/login?next=/periodo/dinos/votacion')

    def test_nombre_url_dinos_votacion(self):
        self.user_login()
        response = self.client.get(reverse('lista_dinos_votacion'))
        self.assertEqual(response.status_code, 200)

    def test_template_dinos_votacion(self):
        self.user_login()
        response = self.client.get('/periodo/dinos/votacion')
        self.assertTemplateUsed(response, 'dinosaurios/dinosaurio_lista_votacion.html')

    def test_envio_datos_dino(self):
        self.user_login()
        self.agrega_dino()
        response = self.client.get('/periodo/dinos/votacion')
        self.assertIn('object_list', response.context)

    def test_envio_t_rex_datos_dino(self):
        self.user_login()
        self.agrega_dino()

        response = self.client.get('/periodo/dinos/votacion')
        self.assertEquals('T-Rex', response.context['object_list'][0]['dino'].nombre)

    def test_t_rex_se_encuentre_en_template(self):
        self.user_login()
        self.agrega_dino()
        response = self.client.get('/periodo/dinos/votacion')
        self.assertContains(response, 'T-Rex')
       
    def test_t_rex_se_encuentre_en_template_en_un_td(self):
        self.user_login()
        self.agrega_dino()
        response = self.client.get('/periodo/dinos/votacion')
        self.assertInHTML('<td>T-Rex</td>',response.rendered_content)


    def test_t_rex_calificacion_4_estrellas(self):
        usuario = self.user_login()
        dino = self.agrega_dino()
        votacion = VotacionDino.objects.create(
            dinosaurio = dino,
            usuario = usuario,
            calificacion = 4,
            rollo = 'me pareció muy chido el dino'
        )
        response = self.client.get('/periodo/dinos/votacion')
        self.assertInHTML('<td>4.0 calificación</td>',response.rendered_content)

    def test_t_rex_calificacion_3_estrellas(self):
        usuario = self.user_login()
        dino = self.agrega_dino()
        votacion = VotacionDino.objects.create(
            dinosaurio = dino,
            usuario = usuario,
            calificacion = 3.0,
            rollo = 'me pareció muy chido el dino'
        )
        response = self.client.get('/periodo/dinos/votacion')
        self.assertInHTML('<td>3.0 calificación</td>',response.rendered_content)

    def test_t_rex_calificacion_3_estrellas(self):
        usuario = self.user_login()
        dino = self.agrega_dino()
        votacion = VotacionDino.objects.create(
            dinosaurio = dino,
            usuario = usuario,
            calificacion = 3,
            rollo = 'me pareció muy chido el dino'
        )
        usuario = User.objects.create(username='juan', password='alex123')
        votacion = VotacionDino.objects.create(
            dinosaurio = dino,
            usuario = usuario,
            calificacion = 5,
            rollo = 'me pareció muy chido el dino'
        )
        response = self.client.get('/periodo/dinos/votacion')
        self.assertInHTML('<td>4.0 calificación</td>',response.rendered_content)

    def test_t_rex_calificacion_0_estrellas(self):
        usuario = self.user_login()
        dino = self.agrega_dino()
        response = self.client.get('/periodo/dinos/votacion')
        self.assertInHTML('<td>0 calificación</td>',response.rendered_content)

    def test_t_rex_calificacion_3_estrellas_img(self):
        usuario = self.user_login()
        dino = self.agrega_dino()
        votacion = VotacionDino.objects.create(
            dinosaurio = dino,
            usuario = usuario,
            calificacion = 3.0,
            rollo = 'me pareció muy chido el dino'
        )
        estrellas = '<td><img src="/static/images/star-filled.svg" class="voto-img"><img src="/static/images/star-filled.svg" class="voto-img">'
        estrellas += '<img src="/static/images/star-filled.svg" class="voto-img"><img src="/static/images/star-empty.svg" class="voto-img">'
        estrellas += '<img src="/static/images/star-empty.svg" class="voto-img"></td>'
        response = self.client.get('/periodo/dinos/votacion')
        self.assertInHTML(estrellas,response.rendered_content)

    def agrega_periodo(self):
        return Periodo.objects.create(nombre = 'Cretacio')

    def agrega_dino(self):
        return Dinosaurio.objects.create(
            nombre = 'T-Rex',
            altura = 5.5,
            periodo = self.agrega_periodo()

        )  
    def user_login(self):
        usuario = User.objects.create_user(username='alex', password='alex123')
        self.client.login(username='alex', password='alex123')
        return usuario
    
