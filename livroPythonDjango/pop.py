lista_usuarios = []
lista_usuarios.append('francisco')
lista_usuarios.append('fulana')
lista_usuarios.append('cicrana')
lista_usuarios.append('beltrano')

print('Conteúdo inicial da lista: ')
print(lista_usuarios)

print('Removendo último elemento da lista: ')
lista_usuarios.pop()
print(lista_usuarios)

print('Removendo o elemento de indice 1: ')
print(lista_usuarios.pop(1), 'foi removido(a) da lista.')
print(lista_usuarios)