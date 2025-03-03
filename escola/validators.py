import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
    cpf = CPF()
    return not cpf.validate(numero_cpf)

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, celular)
    return not response