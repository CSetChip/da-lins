from desafio1.funcoes_d1 import execucao_d1
from desafio2.funcoes_d2 import execucao_d2
from desafio3.funcoes_d3 import execucao_d3
from desafio4.funcoes_d4 import execucao_d4
from desafio5.funcoes_d5 import execucao_d5

try:
    print("Gravando em informações nos arquivos txt")

    execucao_d1()
    print("Arquivo etapa-1.txt gravados com sucesso")

    execucao_d2()
    print("Arquivo etapa-2.txt gravados com sucesso")

    execucao_d3()
    print("Arquivo etapa-3.txt gravados com sucesso")

    execucao_d4()
    print("Arquivo etapa-4.txt gravados com sucesso")

    execucao_d5()
    print("Arquivo etapa-5.txt gravados com sucesso")

    print("Arquivos gravados com sucesso")
except ValueError:
        print("Erro ao tentar gravar arquivos") 


