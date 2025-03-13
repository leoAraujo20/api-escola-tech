from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante01 = Estudante.objects.create(
            nome = 'Teste estudante um',
            email = 'testeestudante01@gmail.com',
            cpf ='68224431002',
            data_nascimento='2024-01-02',
            celular = '86 99999-9999'
        )
        self.estudante02 = Estudante.objects.create(
            nome = 'Teste estudante dois',
            email = 'testeestudante02@gmail.com',
            cpf ='70261486055',
            data_nascimento='2024-01-02',
            celular = '86 99999-9999'
        )

    def test_listar_estudantes(self):
        response = self.client.get(self.url)
        estudantes = Estudante.objects.all()
        serializer = EstudanteSerializer(estudantes, many=True)
        self.assertEqual(response.data['results'], serializer.data)
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
