from manipulando_csv import abrir_csv, escrever_csv

def ator_com_maior_numero_de_filmes(filmes_dos_autores, nome_ator, numero_filmes):
    for ator, num_filme in filmes_dos_autores:
        if num_filme > numero_filmes:
            nome_ator = ator
            numero_filmes = num_filme
    return nome_ator, numero_filmes

def tratar_lista_filme_dos_atores(csv_dados, coluna_atores, coluna_filme):
    filmes_dos_atores = []

    for row in csv_dados[1:]:
        ator = row[coluna_atores]
        num_filme_str = row[coluna_filme]
        
        try:
            num_filme = int(num_filme_str)
        except ValueError:
            continue 
        
        filmes_dos_atores.append((ator, num_filme))

    return filmes_dos_atores

def execucao_d1():
    csv_dados,colunas, data = abrir_csv('csv/actors.csv')

    coluna_filme = colunas.index('Number of Movies')
    coluna_atores = movies_index = colunas.index('Actor')

    filmes_dos_atores = tratar_lista_filme_dos_atores(csv_dados, coluna_atores, coluna_filme)

    nome_do_ator = ''
    numero_filmes = 0

    nome_do_ator, numero_filmes = ator_com_maior_numero_de_filmes(filmes_dos_atores, nome_do_ator, numero_filmes)

    texto = (f'O ator {nome_do_ator} com {numero_filmes} filmes.')

    escrever_csv('etapas_txt/etapa-1.txt', texto)