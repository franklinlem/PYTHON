#Chamando funções
"""Importação do módulo matemático e leitura das variáveis de entrada do problema"""
import math
a = int(input('Digite o coeficiente de a: '))
b = int(input('Digite o coeficiente de b: '))
c = int(input('Digite o coeficiente de c: '))

#Função para calcular o valor de Delta
def delta (a, b, c):
    resultado = (b ** 2) - (4 * a * c)
    return resultado

#Função para calcular o valor da Primeira Raiz
def raiz1(a, b, c):
    resultado = (-b + math.sqrt(delta(a, b, c)))/(2 * a)
    return resultado

#Função para calcular o valor da Segunda Raiz
def raiz2(a, b, c):
    resultado = (-b - math.sqrt(delta(a, b, c)))/(2 * a)
    return resultado

print(f'Delta é: {delta(a, b, c)}')

#Verifica raizes reais:
discriminante = delta(a, b, c)
if discriminante < 0.0:
    print('A equação não tem raízes reais!')
elif discriminante == 0.0:
    raiz = raiz1(a, b, c)
    print(f'A equação possui duas raízes idênticas. de valor {raiz}.')
else:
    raiz1 = raiz1(a, b, c) # type: ignore
    raiz2 = raiz2(a, b, c) # type: ignore
    print(f'A equação possui duas raízes reais, de valores {raiz1} e {raiz2}')