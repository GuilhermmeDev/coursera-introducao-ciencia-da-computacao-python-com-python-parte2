def busca(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

lista = [1,2,3,4,5]
busca(lista,5)