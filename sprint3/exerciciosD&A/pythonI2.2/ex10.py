def remover_repeticoes(lista):
    return list(set(lista))


lista_antiga = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

nova_lista = remover_repeticoes(lista_antiga)

print(nova_lista)