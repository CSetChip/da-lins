def imprimir(*valores_posicionais, **valores_nomeados):

    for vp in valores_posicionais:
        print(vp)

    for chave, valor in valores_nomeados.items():
        print(valor)


imprimir(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)