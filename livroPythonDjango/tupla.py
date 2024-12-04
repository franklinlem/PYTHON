#Tuplas são listas imutáveis

#É possível converter uma lista em tupla por meio de typecast:
lista_animais = ['cachorro', 'gato', 'papagaio']
tupla_animais = tuple(lista_animais)

#não use! irá reconhecer como apenas uma string e não uma tupla!
tupla = ('Python rules!')
print(tupla)
#use tupla assim, com uma virgula depois da string
tupla = ('Python rules!',)
print(tupla)