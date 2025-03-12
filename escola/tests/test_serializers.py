from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class EstudanteSerializerTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome='João da Silva',
            email='joaosilva@gmail.com',
            cpf='68195899056',
            data_nascimento='2023-02-02',
            celular='86 99999-9999'
        )

        self.serializer = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_estudante(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))
    
    def test_verifica_dados_serializados_estudante(self):
        data = self.serializer.data
        self.assertEqual(data['nome'], 'João da Silva')
        self.assertEqual(data['email'], 'joaosilva@gmail.com')
        self.assertEqual(data['cpf'], '68195899056')
        self.assertEqual(data['data_nascimento'], '2023-02-02')
        self.assertEqual(data['celular'], '86 99999-9999')

class CursoSerializerTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo='CTT1',
            descricao='Curso de Teste',
            nivel='I'
        )

        self.serializer = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados_curso(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'codigo', 'descricao', 'nivel']))

    def test_verifica_dados_serializados_curso(self):
        data = self.serializer.data
        self.assertEqual(data['codigo'], 'CTT1')
        self.assertEqual(data['descricao'], 'Curso de Teste')
        self.assertEqual(data['nivel'], 'I')

class MatriculaSerializerTestCase(TestCase):
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

        self.serializer = MatriculaSerializer(instance=self.matricula)

    def test_verifica_campos_serializados_matricula(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'estudante', 'curso', 'periodo']))
    
    def test_verifica_dados_serializados_matricula(self):
        data = self.serializer.data
        print(data)
        self.assertEqual(data['estudante'], self.estudante.id)
        self.assertEqual(data['curso'], self.curso.id)
        self.assertEqual(data['periodo'], self.matricula.periodo)

