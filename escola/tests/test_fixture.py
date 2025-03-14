from django.test import TestCase
from escola.models import Estudante,Curso

class FixtureTextCase(TestCase):
    fixtures = ['banco_test.json']

    def test_carregamento_fixture(self):
        estudante = Estudante.objects.get(pk=3)
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.nome, 'Ana Beatriz Lima')
        self.assertEqual(curso.codigo, 'PO01')