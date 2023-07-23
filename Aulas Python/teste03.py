print('inicio do programa')
L = []
x = float(input('Digite um número real: '))
while x != 0:
    L.append('{:.3f}\n'.format(x))
    x = float(input('Digite um número real: '))
arq = open('NumReal.txt', 'w')
arq.writelines(L)
arq.close()
print(L)
print('fim do programa')