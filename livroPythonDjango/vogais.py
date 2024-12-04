vogais=['a','e','i','o','u','A','E','I','O','U']

lista=[]

entrada=input('Digite uma palavra a ser filtrada: ')

for letra in entrada:
    if letra not in vogais:
        lista.append(letra)
if len(lista) > 0:
    print(f'A palavra {entrada} possui {len(lista)} caracteres que não são vogais!')
else:
    print(f'A palavra {entrada} possui apenas vogais!')
