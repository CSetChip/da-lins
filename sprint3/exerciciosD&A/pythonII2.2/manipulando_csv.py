def abrir_csv(nome_csv):
    with open(nome_csv, 'r', newline='', encoding='utf-8') as csv:
        csv_dados = [line.split(',') for line in csv.read().splitlines()]
        colunas = csv_dados[0]
        data_lines = csv_dados[1:]

        return csv_dados, colunas, data_lines

def escrever_csv(nome_csv,texto):
    with open(nome_csv, 'w', encoding='utf-8') as output_file:
        output_file.write(texto)

def escrever_csv_lista_para_d4(nome_csv, lista):
    with open(nome_csv, 'w', encoding='utf-8') as output_file:
        sequencia = 1
        for filme, contagem in lista:
            output_file.write(f'{sequencia} - O filme {filme} aparece {contagem} vez(es) no dataset\n')
            sequencia += 1

def escrever_lista_csv_para_d5(nome_csv, lista):
    with open(nome_csv, 'w', encoding='utf-8') as output_file:
        for ator, receita in lista:
            output_file.write(f'{ator} - {receita:.2f}\n')
