from django.test import TestCase
from escola.models import Estudante

class EstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail("Teste falhou :(")

    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='João da Silva',
            email='joaosilva@gmail.com',
            cpf='68195899056',
            data_nascimento='2023-02-02',
            celular='86 99999-9999'
        )
    
    def test_checa_atributos_estudante(self):
        self.assertEqual(self.estudante.nome, 'João da Silva')
        self.assertEqual(self.estudante.email, 'joaosilva@gmail.com')
        self.assertEqual(self.estudante.cpf, '68195899056')
        self.assertEqual(self.estudante.data_nascimento, '2023-02-02')
        self.assertEqual(self.estudante.celular, '86 99999-9999')