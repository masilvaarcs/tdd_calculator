"""
calculator.py

Este módulo contém funções para realizar operações matemáticas básicas, como soma, subtração,
multiplicação e divisão.
"""


def soma(numero_a, numero_b):
    """
    Função que realiza a soma de dois números inteiros.

    Args:
        numero_a (int): O primeiro número inteiro a ser somado.
        numero_b (int): O segundo número inteiro a ser somado.

    Returns:
        int: O resultado da soma de numero_a e numero_b.
    """
    return numero_a + numero_b


def subtrai(numero_a, numero_b):
    """
    Função que realiza a subtração de dois números inteiros.

    Args:
        numero_a (int): O número inteiro a ser subtraído.
        numero_b (int): O número inteiro que será subtraído.

    Returns:
        int: O resultado da subtração de numero_b de numero_a.
    """
    return numero_a - numero_b


def multiplica(numero_a, numero_b):
    """
    Função que realiza a multiplicação de dois números inteiros.

    Args:
        numero_a (int): O primeiro número inteiro a ser multiplicado.
        numero_b (int): O segundo número inteiro a ser multiplicado.

    Returns:
        int: O resultado da multiplicação entre numero_a e numero_b.
    """
    return numero_a * numero_b


def divide(numero_a, numero_b):
    """
    Função que realiza a divisão de dois números inteiros.

    Args:
        numero_a (int): O número inteiro a ser dividido (dividendo).
        numero_b (int): O número inteiro pelo qual a divisão será feita (divisor).

    Returns:
        float: O resultado da divisão de numero_a por numero_b.
    """
    return numero_a / numero_b
