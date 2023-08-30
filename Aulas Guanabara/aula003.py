"""CADEIA DE CARACTERES - STRINGS"""

frase = "Curso em Video Python"
print(frase[9:14])
print(frase[0:20:2])
nome = str(input("Qual é o seu nome completo?")).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
