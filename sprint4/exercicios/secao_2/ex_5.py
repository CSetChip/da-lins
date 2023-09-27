import csv

def calcular_media_tres_maiores(notas):
    return round(sum(sorted(notas, reverse=True)[:3]) / 3, 2)

def formatar_media(media):
    return f"{int(media):.1f}" if media % 1 == 0 else f"{media:.2f}"

def processar_linha(linha):
    nome, *notas = linha
    notas_int = list(map(int, notas))
    return (nome, notas_int, formatar_media(calcular_media_tres_maiores(notas_int)))

with open('exercicios/secao_2/arquivos/estudantes.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    lista_alunos = sorted(map(processar_linha, leitor_csv), key=lambda x: x[0])

for nome, notas, media_formatada in lista_alunos:
    notas_ordenadas = sorted(notas, reverse=True)
    print(f"Nome: {nome} Notas: {notas_ordenadas[0:3]} Média: {media_formatada}")

