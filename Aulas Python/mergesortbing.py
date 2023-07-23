def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    lista_esquerda = lista[:meio]
    lista_direita = lista[meio:]

    lista_esquerda = merge_sort(lista_esquerda)
    lista_direita = merge_sort(lista_direita)

    return merge(lista_esquerda, lista_direita)

def merge(lista_esquerda, lista_direita):
    if not lista_esquerda:
        return lista_direita

    if not lista_direita:
        return lista_esquerda

    if lista_esquerda[0] < lista_direita[0]:
        return [lista_esquerda[0]] + merge(lista_esquerda[1:], lista_direita)

    return [lista_direita[0]] + merge(lista_esquerda, lista_direita[1:])