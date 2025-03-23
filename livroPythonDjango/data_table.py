import pprint

produtos= {}

produtos[1] = {
    'descricao': 'Mouse óptico sem fio',
    'preco': 50.0,
    'estoque': 130
}
produtos[2] = {
    'descricao': 'Teclado USB',
    'preco': 42.0,
    'estoque': 100
}

produtos[3] = {
    'descricao': 'Monitor colorido 20 pol.',
    'preco': 850.0,
    'estoque': 20
}

produtos[4] = {
    'descricao': 'Par de caixas de som',
    'preco': 90.0,
    'estoque': 17
}

#print(produtos)

pprint.pprint(produtos)

#Funções get(), items(), values(), clear()
print(produtos.get(1))
print(produtos.items())
print(produtos.values())
print(produtos.get(1).values())
produtos.clear()
print(produtos)