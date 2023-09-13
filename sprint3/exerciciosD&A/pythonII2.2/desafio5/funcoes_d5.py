from manipulando_csv import escrever_lista_csv_para_d5, abrir_csv

def tratando_lista_receita_atores(colunas, data_lines):
    atores = []

    indice_ator = colunas.index('Actor')
    indice_total_gross = colunas.index('Total Gross')

    for linha in data_lines:
        valores = linha
    
        nome_ator = valores[indice_ator]
        receita_bruta = valores[indice_total_gross].replace('$', '').replace(',', '')
        
        try:
            receita_bruta = float(receita_bruta)
        except ValueError:
            continue 

        atores.append((nome_ator, receita_bruta))

    atores_ordenados = sorted(atores, key=lambda x: x[1], reverse=True)

    return atores_ordenados

def execucao_d5():
    csv_dados,colunas, data_lines = abrir_csv('csv/actors.csv')

    atores_ordenados = tratando_lista_receita_atores(colunas, data_lines)

    escrever_lista_csv_para_d5('etapas_txt/etapa-5.txt', atores_ordenados)