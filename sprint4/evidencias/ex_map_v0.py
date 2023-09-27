lista_pessoas = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'Jose', 'idade': 26}
]

so_nomes = map(lambda p: p['nome'], lista_pessoas)
# print(list(so_nomes))

so_idades = map(lambda p: p['idade'], lista_pessoas)
# print(list(so_idades))

informacoes = map(lambda p: f"{p['nome']} tem {p['idade']}", lista_pessoas)

print(list(informacoes))
