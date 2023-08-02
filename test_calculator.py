# test_calculator.py

"""
Implementação de testes para reforçar a necessidade e importância no desenvolvimento.
"""

import calculator


# Implementação para teste da função soma
def test_soma():
    """
    Testa a função soma do módulo calculator.py.
    Verifica se a função soma retorna o resultado correto.
    """
    result = calculator.soma(2, 3)
    assert result == 5, "A soma de 2 e 3 deve ser 5"


# Implementação para teste da função subtrai
def test_subtrai():
    """
    Testa a função subtrai do módulo calculator.py.
    Verifica se a função subtrai retorna o resultado correto.
    """
    result = calculator.subtrai(27, 10)
    assert result == 17, "A subtração de 27 e 10 deve ser 17"


# Implementação para teste da função multiplica
def test_multiplica():
    """
    Testa a função multiplica do módulo calculator.py.
    Verifica se a função multiplica retorna o resultado correto.
    """
    result = calculator.multiplica(3, 6)
    assert result == 18, "A multiplicação de 3 por 6 deve ser 18"


# Implementação para teste da função divide
def test_divide():
    """
    Testa a função divide do módulo calculator.py.
    Verifica se a função divide retorna o resultado correto.
    """
    result = calculator.divide(27, 3)
    assert result == 9, "A divisão de 27 por 3 deve ser 9"
