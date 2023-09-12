import datetime

nome = input("Nome: ")
idade = int(input("Idade: "))

if idade < 0:
    print("A idade não pode ser negativa")
else:
    ano_atual = datetime.date.today().year
    cem_anos = ano_atual + (100 - idade)
    
    print(cem_anos)