def busca_binaria_rec(lista, chave, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == chave:
        return meio
    if chave < lista[meio]:
        return busca_binaria_rec(lista, chave, inicio, meio - 1)
    else:
        return busca_binaria_rec(lista, chave, meio + 1, fim)

def busca_binaria(lista, chave):
    tam = len(lista)
    inicio = 0
    fim=tam-1

    while inicio<=fim:
        meio=(inicio+fim)//2
        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            inicio=meio+1
        elif lista[meio] > chave:
            fim = meio-1

    return -1

lista = [8,2,5,1,9,10,17,15]
lista.sort()
print(lista)
#res = busca_binaria(lista, 1)
res = busca_binaria_rec(lista, 100, 0, len(lista)-1)
print(res)