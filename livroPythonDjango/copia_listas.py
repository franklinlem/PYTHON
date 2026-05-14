#copiando listas

lista_documentos=['doc1', 'doc2', 'doc3', 'doc4']

print('Copiando da forma errada...')
lista_tmp = lista_documentos #lista_tmp não copia, apenas aponta(faz referência) para os itens da lista_documentos
print(f'lista_documentos = {lista_documentos}')
print(f'lista_tmp = {lista_tmp}')

print('Alterando elemento de lista_documentos e verificando novamente...')
lista_documentos[2] = 'doc10'
print(f'lista_documentos = {lista_documentos}')
print(f'lista_tmp = {lista_tmp}')
print('As variáveis estão apontando para a mesma lista!')

print('Corrigindo o problema...')
lista_tmp = lista_documentos.copy()

print('Alterando elemento de lista_documentos e verificando novamente...')
lista_documentos[2]='doc3'
print(f'lista_documentos = {lista_documentos}')
print(f'lista_tmp = {lista_tmp}')
