def dividir_lista(lista):
    valor_div = len(lista) // 3
    lista1 = lista[:valor_div]
    lista2 = lista[valor_div:2 * valor_div]
    lista3 = lista[2 * valor_div:]
    return lista1, lista2, lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1, lista2, lista3 = dividir_lista(lista)

print(lista1, lista2, lista3)