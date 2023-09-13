from manipulando_csv import abrir_csv, escrever_csv
import statistics

def calcular_media(csv_dados, coluna_total_gross):
    list_gross = []

    for row in csv_dados[1:]:
        gross = row[coluna_total_gross].strip()

        try:
            valor_gross = float(gross.replace(',', '').replace('$', ''))
            list_gross.append(valor_gross)
        except ValueError:
            continue
    return list_gross

def formatar_media(list_gross):
    media = statistics.mean(list_gross)

    media_formatada = "{:.2f}".format(media)

    media_formatada_sem_ponto = media_formatada.replace('.', '')

    return media_formatada_sem_ponto[:2] + '.' + media_formatada_sem_ponto[2:]

def execucao_d2():
    csv_dados,colunas, data = abrir_csv('csv/actors.csv')

    coluna_total_gross = colunas.index('Gross')

    list_gross = calcular_media(csv_dados, coluna_total_gross)
        
    media_final = formatar_media(list_gross)

    texto = (f'A média da coluna Gross é aproximadamente {media_final}')

    escrever_csv('etapas_txt/etapa-2.txt', texto)