import pytest
from app.validacao import validar_cpf

def test_cpf_valido_sem_formatacao():
    assert validar_cpf("52998224725") == True

def test_cpf_valido_com_formatacao():
    assert validar_cpf("529.982.247-25") == True

def test_cpf_invalido_todos_digitos_iguais():
    assert validar_cpf("11111111111") == False

def test_cpf_invalido_tamanho_menor():
    assert validar_cpf("1234567890") == False

def test_cpf_invalido_tamanho_maior():
    assert validar_cpf("123456789012") == False

def test_cpf_invalido_digitos_verificadores():
    assert validar_cpf("52998224735") == False

def test_cpf_invalido_caracteres_nao_numericos():
    assert validar_cpf("ABC529982247") == False

def test_cpf_valido_gerado_aleatoriamente():
    assert validar_cpf("45317828791") == True

def test_cpf_invalido_zeros():
    assert validar_cpf("00000000000") == False

def test_cpf_valido_outro_exemplo():
    assert validar_cpf("12345678909") == True  # CPF conhecido como válido para testes