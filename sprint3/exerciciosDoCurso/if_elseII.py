def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor De Idade'
    elif 18 <= idade < 65:
        return 'Adulto'
    elif 65 <= idade < 100:
        return 'Melhor Idade'
    elif idade >= 100:
        return 'Centenário'
    else: 
        return 'Idade invalida'
    
if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -2):
        print(f'{idade} : {faixa_etaria(idade)}')
