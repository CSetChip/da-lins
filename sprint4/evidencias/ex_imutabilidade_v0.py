from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR.utf8')

index_meses = filter(lambda mes: mdays[mes] == 31, range(1,13))
nomes_index = map(lambda mes: month_name[mes], index_meses)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos} \n- {nome_mes}', nomes_index, 'Meses com 31 dias:')
print(juntar_meses)

#Opção alternativa

def mes_com_31(mes): return mdays[mes] == 31

def get_nome_mes(mes): return month_name[mes]

def juntar_meses(todos, nome_mes): return f'{todos} \n- {nome_mes}'

print(reduce(juntar_meses, 
            map(get_nome_mes, filter(mes_com_31, range(1,13))),
            'Meses com 31 dias:'))

