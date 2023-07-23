def busca_binaria(l, x, incio, fim):
    meio = (inicio + fim) // 2

    if fim < inicio:
        return -1

    if x == l(meio):
        return meio

    if x < l(meio):
        return busca_binaria(l, x, incio, meio -1)

    if x> l(meio):
        return busca_binaria(l, x, meio + 1, fim)
