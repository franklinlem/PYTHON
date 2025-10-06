"""Exemplo de variável global"""

x = "123"       #Definição fora do corpo da funçã - variável global

def testar()->None:
    print(f'Valor de x dentro da função testar(): {x}')

testar()
print(f'Valor de x fora da função testar(): {x}')