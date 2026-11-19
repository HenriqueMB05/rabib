import math as m

def soma(a: float, b:float) -> float:
    return a + b

def subtaçao(a: float, b:float) -> float:
    return a - b

def multiplicaçao(a: float, b:float) -> float:
    return a * b

def divisao(a: float, b:float) -> float:
    if  b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

def potencia(a: float, b:float) -> float:
    return m.pow(a, b)

def raiz_quadrada(a: float) -> float:
    if a < 0:
        raise ValueError("Nao é possivel calcular a raiz quadrada de um numero negativo")
    return m.sqrt(a)