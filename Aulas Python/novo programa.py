print("Novo Programa")
g='gravação e leitura de txt'
arq=open('exemplo01.txt', 'w')
arq.write(g)
arq.close()
arq=open('exemplo01.txt', 'r')
l=arq.readline()
arq.close()
print('string lido = {}' .format(l))
print('fim do programa')