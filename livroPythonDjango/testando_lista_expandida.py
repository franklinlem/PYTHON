#Funções personalizadas
impares = [1,3,5,7,9]

def sao_impares(*lista):
    resultado = True
    for num in lista:
        if (num % 2) == 0:
            resultado = False
    return resultado

print(sao_impares(1,3,5,7,9))

"""Convertendo parametros em um dicionario

def altera_registro(**kwargs):
    nome = kwargs['nome']
    codigo = kwargs['codigo']

altera_registro(
    codigo = 1,
    nome = 'Francisco'
)

registro = {
    'codigo':1,
    'nome':'Francisco'
}

altera_registro(**registro)
"""