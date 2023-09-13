from manipulando_csv import escrever_csv_lista_para_d4, abrir_csv

def contagem_de_filmes(data_lines, coluna_actor):
    contagem_filmes = {}

    for linha in data_lines:
        filme = linha[coluna_actor]

        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            contagem_filmes[filme] = 1

    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: x[1], reverse=True)

    return filmes_ordenados

def execucao_d4():
    csv_dados,colunas, data_lines = abrir_csv('csv/actors.csv')

    coluna_actor = colunas.index('#1 Movie')
    
    filmes_ordenados = contagem_de_filmes(data_lines, coluna_actor)
    
    escrever_csv_lista_para_d4('etapas_txt/etapa-4.txt', filmes_ordenados)





