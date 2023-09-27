with open('exercicios/secao_2/arquivos/numeros.txt', 'r') as arquivo:
    cinco_maiores = sorted(list(filter(lambda x: x % 2 == 0, list(map(int, arquivo.readlines())))), reverse=True)[:5]
    print(f'Sequencia dos maiores: {cinco_maiores}\nSoma: {sum(cinco_maiores)}')
