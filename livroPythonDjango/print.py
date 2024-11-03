#comando print

print("Ser ou não ser")
print("Eis a questão")

print("Ser ou não ser \nEis a questão")

#\n = nova linha
#\t = uma tabulação
#\r = enter
#\+(caracter especial: ' " \ $)

#repetição de strings
#print("\n" * 100) #repete linha em branco 100 vezes

"""operador de formatação de strings (%)
%d ou %i = inteiro com sinal
%f = numero decimal (float)
%o = valor de base octal, converte para octal
%x = valor de base hexadecimal, converte para hexadecimal
%s = imprime um texto literal na posição
%% = exibe um sinal de porcentagem na posição
%.(+numero de casas decimais) = imprime numero decimal com quantidade de casas solicitadas
"""

#exemplos com %
print("Hoje é dia %d" %15)
print("12 em octal é %o" %12)
print("255 em hexadecimal é %x" %255)
print("pi com duas casa decimais é %.2f" %3.1415926)
nome = "Francisco"
print("Meu nome é %s" %nome)

print("Constantes - pi: %.2f e: %.2f" %(3.1415926, 2.718281))

#interpolação de strings f'String {expressao}'
print(f"Nome do usuario: {nome}")
print(f"A média aritmética entre 5 e 9 é: {(5+9)/2}")

#parametro "end" evita quebra automática de linha
print("Ser ou não ser, ", end="")
print('Eis a questão. ')

#parametro "sep" separa valores de uma lista
print(" um", "dois", "tres", "quatro", 5, sep="\n ")

print("brasil" + "eiro") #concatenação de strings