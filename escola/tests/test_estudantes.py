from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)