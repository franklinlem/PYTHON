#imprimir elementos em ordem inversa

turma=['Alice','Bob','Carl','Daniele','Eduard','Felicia']
print('\n', turma)

print('\n\nLista original: ')
for aluno in turma:
    print(aluno, end=' ')

print('\n\n\"Fatiando\" os quatro primeiros de dois em dois, ordem inversa: ')
for indice in range(3, 0, -2):
    print(turma[indice], end=' ')

print('\n\nIgnorando os 2 primeiros na ordem inversa: ')
for indice in range(len(turma)-1, 1, -1):
    print(turma[indice], end=' ')

print('\n\nPegando os últimos 5 elementos na ordem inversa: ')
for indice in range(5, 0, -1):
    print(turma[indice], end=' ')

print('\n\nRetornando todo mundo de 2 em 2 a parti do fim (índices pares): ')
for indice in range(len(turma)-2, -1, -2):
    print(turma[indice], end=' ')

print('\n\nRetornando todo mundo de 2 em 2 a parti do fim (índices ímpares): ')
for indice in range(len(turma)-1, -1, -2):
    print(turma[indice], end=' ')
