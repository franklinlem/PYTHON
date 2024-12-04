lista=['Alice','Bob','Carl','Bob','Alice','Bob','Carl','Alice']
print(f'\nConteúdo inicial da lista: {lista}')

print('\nConvertendo a lista em conjunto para eliminar duplicidades...')
s1=set(lista)
print('\nConvertendo o conjunto em uma lista sem duplicações...')
lista_nova = list(s1)
print(f'\nConteúdo da lista sem valores duplicados: {lista_nova}')
