def mapear(funcao, lista):
    return (funcao(i) for i in lista)

if __name__ == '__main__':
    print(list(mapear(lambda x : x ** 2 , [2,3,4])))