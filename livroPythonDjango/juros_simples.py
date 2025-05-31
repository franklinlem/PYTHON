#Função para calcular juros simples

def calcula_juros(principal, meses, taxa):
    resultado = (principal * taxa * meses) / 100
    return resultado

print('Calculando os juros de R$ 100,00 a 5% por 3 meses: ')
print(f'R$ {calcula_juros(100.0,5,3)}')