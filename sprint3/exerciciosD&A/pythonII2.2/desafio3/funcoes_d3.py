from manipulando_csv import abrir_csv, escrever_csv

def calculando_media_ator(data_lines, coluna_actor, coluna_media_por_filme):
    melhor_media = 0
    melhor_ator = ''

    for line in data_lines:

        valores = line
    
        nome = valores[coluna_actor]
        
        media_por_filme = valores[coluna_media_por_filme].strip().replace(',', '').replace('$', '')

        try:
            media_por_filme = float(media_por_filme)
        except ValueError:
            continue

        if media_por_filme > melhor_media:
            melhor_media = media_por_filme
            melhor_ator = nome

    return melhor_ator, "{:.2f}".format(melhor_media).replace(".", "")

def execucao_d3():
    csv_dados,colunas, data_lines = abrir_csv('csv/actors.csv')

    coluna_actor = colunas.index('Actor')
    coluna_media_por_filme = colunas.index('Average per Movie')

    melhor_ator, melhor_media_formatada = calculando_media_ator(data_lines, coluna_actor, coluna_media_por_filme)

    texto = (f'O ator {melhor_ator} com a media de {melhor_media_formatada}')

    escrever_csv('etapas_txt/etapa-3.txt', texto)