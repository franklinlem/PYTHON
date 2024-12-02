#Programa que solicita ao usuario que digite o seu login e, em seguida, verifica se esse login está de acordo com as seguintes regras: inicia com uma letra maiuscula, tem no mínimo 6 caracteres, possui pelo menos 2 caracteres numéricos, possui pelo menos 3 letras, possui tamanho de até 10 caracteres.

login = ''
login = input('Digite nome de usuario para fazer login: ')

tamanho = len(login)
letras = 0
numeros = 0
maiuscula = login.capitalize()

for letra in login:
    if letra.isdigit():
        numeros = numeros + 1
    if letra.isalpha():
        letras = letras + 1   

if tamanho < 6 or tamanho > 10 or letras < 3 or numeros <2 or login != maiuscula:
    print('Login inválido! \nO nome de usuario deve ter entre 6 e 10 caracteres alfanuméricos. \nDeve ter no mínimo 3 letras e 2 números. \nA primeira letra deve ser maiuscula!')
else:
    print('Bem vindo: ', login)

print('Letras: ', letras)
print('Numeros: ', numeros)
