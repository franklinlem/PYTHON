#imprimir elementos em ordem inversa

turma=['Alice','Bob','Carl','Daniele','Eduard','Felicia']
print('\n', turma)

print('\n\nLista original: ')
for aluno in turma:
    print(aluno, end=' ')

print('\n\n\"Fatiando\" os quatro primeiros de dois em dois, ordem inversa: ')
for indice in range(3, 0, -2):
    print(turma[indice], end=' ')

