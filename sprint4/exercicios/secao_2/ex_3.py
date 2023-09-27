from functools import reduce

def calcula_saldo(lancamentos):
    return reduce(lambda saldo, lancamento: saldo + lancamento[0] * lancamento[1],
        map(lambda lancamento: (lancamento[0], 1 if lancamento[1] == 'C' else -1), lancamentos), 0)

print("Saldo final:", calcula_saldo([(200, 'D'),(300, 'C'),(100, 'C')])) 
