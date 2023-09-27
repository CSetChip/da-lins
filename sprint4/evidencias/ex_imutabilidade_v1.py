from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

print('Lista orignal: ', valores)
print('Lista ordenada: ', sorted(valores))
print('Menor valor da lista: ', min(valores))
print('Maior valor da lista: ', max(valores))
print('Soma dos elementos da lista: ', sum(valores))
print('Lista ao contrario: ', tuple(reversed(valores)))

