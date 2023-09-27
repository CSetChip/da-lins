def calcular_valor_maximo(operadores, operandos) -> float:
    def aplicar_operacao(operador, operandos):
        if operador == '+':
            return operandos[0] + operandos[1]
        elif operador == '-':
            return operandos[0] - operandos[1]
        elif operador == '*':
            return operandos[0] * operandos[1]
        elif operador == '/':
            return operandos[0] / operandos[1]
        elif operador == '%':
            return operandos[0] % operandos[1]
    
    return max(map(lambda x: aplicar_operacao(x[0], x[1]), zip(operadores, operandos)))

operadores = ['+','-','*','/','+']
operandos = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)

