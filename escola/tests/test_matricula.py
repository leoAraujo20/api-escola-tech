from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from escola.models import Estudante, Curso, Matricula
from escola.serializers import MatriculaSerializer

class MatriculasTestCase(APITestCase):
    fixtures = ['banco_test.json']

    def setUp(self):
        self.usuario = User.objects.get(username='leonidas')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.get(pk=1)
        self.curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.get(pk=1)
    
    def test_listar_matriculas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_criar_matricula(self):
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'M'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_atualizar_matricula(self):
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'V'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_remover_matricula(self):
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
    