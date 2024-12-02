texto = 'TinhaUmaPedraNoMeioDoCaminho'
if texto.isalpha():
    print('O texto %s, contém apenas caracteres alfabéticos!' % texto)
else:
    print('O texto %s, contém caracteres não alfabéticos!' % texto)

texto = "Rua Alfredo Condeixa, 382."
if str.isalpha(texto):
    print('O texto %s, contém apenas caracteres alfabéticos!' % texto)
else:
    print('O texto %s, contém caracteres não alfabéticos!' % texto)

fone = '(16)974014626'
if str.isdigit(fone):
    print(f'A string {fone} contém apenas números!')
else:
    print(f'A string {fone} contém caracteres não numéricos!')