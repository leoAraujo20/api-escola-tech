from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class EstudanteTestCase(TestCase):
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
    
class CursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo='CTT1',
            descricao='Curso de Teste',
            nivel='I'
        )
    
    def test_checa_atributos_curso(self):
        self.assertEqual(self.curso.codigo, 'CTT1')
        self.assertEqual(self.curso.descricao, 'Curso de Teste')
        self.assertEqual(self.curso.nivel, 'I')

class MatrciculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='João da Silva',
            email='joaosilva@gmail.com',
            cpf='68195899056',
            data_nascimento='2023-02-02',
            celular='86 99999-9999'
        )
        
        self.curso = Curso.objects.create(
            codigo='CTT1',
            descricao='Curso de Teste',
            nivel='I'
        )

        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='N'
        )
    
    def test_checa_atributos_matricula(self):
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, 'N')

