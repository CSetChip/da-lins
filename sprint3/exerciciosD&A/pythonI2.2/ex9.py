primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, (nome, sobrenome, idade) in enumerate(zip(primeirosNomes,sobreNomes, idades)):
    print(f'{indice} - {nome} {sobrenome} está com {idade} anos')