from django.test import TestCase
from dinosaurios.models import Dinosaurio, Periodo


class TestHumo(TestCase):

    def test_prueba_humo(self):
        self.assertEqual(2 + 2, 4)

    def test_agrega_dinosaurio(self):
        periodo = Periodo.objects.create(
            nombre='cretacio',
            descripcion='periodo chido'
        )
        dino = Dinosaurio.objects.create(
            nombre='T-REX',
            altura='5',
            periodo=periodo,
        )
        dino_uno = Dinosaurio.objects.first()

        self.assertEqual(dino_uno, dino)
        self.assertEqual(dino_uno.nombre, 'T-REX')
        self.assertEqual(str(dino_uno), 'T-REX')
        self.assertEqual(len(Dinosaurio.objects.all()), 1)
