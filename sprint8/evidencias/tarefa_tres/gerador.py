import random
import os
import time
import names

def gerador_nomes():
    random.seed(40)
    qtd_nomes_unicos = 3000
    qtd_nomes_aleatorios = 10000000

    aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]
    print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

    dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

    nome_arquivo = "nomes_aleatorios.txt"
    gravador_dados(nome_arquivo, dados, "Nomes\n")
    print(f"Arquivo {nome_arquivo} gerado com sucesso.")

    os.system(f'nano {nome_arquivo}')


def gerador_inteiros():
    inteiros = list(reversed(random.choices(range(1, 1001), k=250)))
    print(inteiros)

def gerador_animais():

    animais = ["Pangolim", "Tamanduá", "Ovelha", "Cabra", "Vaca", "Boi", "Touro", "Cavalo", "Pônei", 
               "Burro", "Lhama", "Alpaca", "Guaxinim", "Urso-preguiça", "Gorila", "Chimpanzé", "Orangotango", 
               "Gibão", "Sagui", "Babuíno"]
    
    animais_ordenados = sorted(animais)
    gravador_dados("animais.csv", animais_ordenados, "Animais \n")

def gravador_dados(nome,informacao,coluna):
    with open(nome, 'w') as arquivo:
        arquivo.write(coluna)
        for i in informacao:
            arquivo.write(f"{i}\n")

