def calculadora (num1, num2, operacao):
    if (operacao==1):
        return num1+num2
    elif (operacao==2):
        return num1-num2
    elif (operacao==3):
        return num1*num2
    elif (operacao==4):
        return num1/num2
    else:
        return 0
x = float(input('1º número: '))
y = float(input('2º número: '))
conta = int(input('selecione o número correspondente à operação desejada:\n1. soma\n2. subtração\n3. multiplicação\n4. divisão\n'))
print(f'resultado: {round(calculadora(x, y, conta), 2)}')
