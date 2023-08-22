nome = input("Digite um nome: ")
print("Digitou: {:^30}".format(nome)) #coloca a variavel no meio de 30 espaços
print("Digitou: {:>30}".format(nome)) #alinha a variavel na direita
print("Digitou: {:=^30}".format(nome)) #centraliza a variável entre sinais de igual(=)
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
print("A soma é {}".format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
ex = n1 ** n2
print("A soma é {}, \no produto é {}, \na divisão é {:.3f}, \na divisão inteira é {} \ne a pontencia equivale a {}.\n".format(s, m, d, di, ex))