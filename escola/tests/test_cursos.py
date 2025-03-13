from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso01 = Curso.objects.create(
            codigo='CT01',
            descricao='Curso Teste 01',
            nivel='B'
        )
        self.curso02 = Curso.objects.create(
            codigo='CT02',
            descricao='Curso Teste 02',
            nivel='A'
        )
    
    def test_listar_cursos(self):
        response = self.client.get(self.url)
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listar_um_curso(self):
        response = self.client.get(f'{self.url}1/')
        curso = Curso.objects.get(pk=1)
        serializer = CursoSerializer(curso)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criar_curso(self):
        data = {
            'codigo': 'CRT01',
            'descricao': 'Curso create',
            'nivel': 'I'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_atualizar_curso(self):
        data = {
            'codigo': 'PUT01',
            'descricao': 'Curso put',
            'nivel': 'A'
        }
        response = self.client.put(f'{self.url}1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remover_curso(self):
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

