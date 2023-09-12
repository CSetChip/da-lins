def my_map(lista, funcao):
    resultado = []
    for elemento in lista:
        resultado.append(funcao(elemento))
    return resultado

def pot(elemento):
    return elemento ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_lista = my_map(lista, pot)

print(nova_lista)