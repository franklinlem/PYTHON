#Percorrendo lista com for e range

turma=['Alice','Bob','Carl','Daniele','Eduard','Felicia']
print('\n', turma)

print('\n\nLista original: ')
for aluno in turma:
    print(aluno, end=' ')

print('\n\n\"Fatiando\" os quatro primeiros de dois em dois: ')
for indice in range(0, 4, 2):
    print(turma[indice], end=' ')

print('\n\nIgnorando os dois primeiros: ')
for indice in range(2, len(turma)):
    print(turma[indice], end=' ')

print('\n\nPegando até o quinto elemento: ')
for indice in range(0, 5):
    print(turma[indice], end=' ')

print('\n\nRetornando todo mundo de 2 em 2 a partir do inicio (indices pares): ')
for indice in range(0, len(turma), 2):
    print(turma[indice], end=' ')

print('\n\nRetornando todo mundo de 2 em 2 a partir do segundo (indices impares): ')
for indice in range(1, len(turma), 2):
    print(turma[indice], end=' ')
