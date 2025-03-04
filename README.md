# API Escola Tech

## Descrição
Esta é a API do projeto Escola Tech, que fornece funcionalidades para gerenciar informações de uma escola de tecnologia.

## Funcionalidades
- Cadastro de alunos
- Gerenciamento de cursos
- Matrícula de alunos em cursos

## Tecnologias Utilizadas
- Python
- Django
- Django REST Framework

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/leoAraujo20/api-escola-tech.git
    ```
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Execute as migrações:
    ```bash
    python manage.py migrate
    ```

## Uso
1. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```
2. Acesse a API em `http://localhost:8000`
