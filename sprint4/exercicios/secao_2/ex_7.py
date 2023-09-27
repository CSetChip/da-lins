def pares_ate(n: int):
    for i in range(2, n + 1, 2):
        yield i

gerador = pares_ate(10)

for numero in gerador:
    print(numero)
