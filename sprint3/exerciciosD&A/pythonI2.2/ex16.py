def soma(valores):
    numeros = valores.split(',')
    resul_soma = 0

    for num in numeros:
        resul_soma += int(num)

    return resul_soma

resultado = soma("1,3,4,6,10,76")
print(resultado)