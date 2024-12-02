lista = ['Lista_A', 'Lista_B', 'Lista_C']
tupla = ('tupla_A', 'tupla_B', 'tupla_C')
dicionario = {'dicionario_A':'1', 'dicionario_B':'2', 'dicionario_C':'3'}

print('Lista: ', lista)
print('Tupla: ', tupla)
print('Dicionário: ', dicionario)

separador = "*"

print('Agora, após o join: ')

print('Lista: ', separador.join(lista))
print('Tupla: ', separador.join(tupla))
print('Dicionário: ', separador.join(dicionario))