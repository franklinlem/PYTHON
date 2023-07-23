import random
n1 = input('aluno1 ')
n2 = input('aluno2 ')
n3 = input('aluno3 ')
n4 = input('aluno4 ')
n5 = input('aluno5 ')
lista = [n1, n2, n3, n4, n5]
random.shuffle(lista)
print(lista)