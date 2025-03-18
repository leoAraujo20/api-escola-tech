from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['banco_test.json']

    def setUp(self):
        self.usuario = User.objects.get(username='leonidas')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante01 = Estudante.objects.get(pk=1)
        self.estudante02 = Estudante.objects.get(pk=2)

    def test_listar_estudantes(self):
        response = self.client.get(self.url)
        estudantes = Estudante.objects.all()
        serializer = EstudanteSerializer(estudantes, many=True)
        self.assertEqual(response.data['results'], serializer.data[:len(response.data['results'])])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listar_um_estudante(self):
        response = self.client.get(f'{self.url}1/')
        estudante = Estudante.objects.get(pk=1)
        serializer = EstudanteSerializer(estudante)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criar_estudante(self):
        data = {
            'nome':'teste',
            'email':'teste@gmail.com',
            'cpf':'82271917034',
            'data_nascimento':'2003-05-04',
            'celular':'11 99999-9999'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_atualizar_estudante(self):
        data = {
            'nome':'teste',
            'email':'teste@gmail.com',
            'cpf':'82271917034',
            'data_nascimento':'2003-05-04',
            'celular':'11 99999-9999'
        }
        response = self.client.put(f'{self.url}1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remover_estudante(self):
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
