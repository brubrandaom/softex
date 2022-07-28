def calculadora (num1, num2, operador):
    if (operador==1):
        return num1+num2
    elif (operador==2):
        return num1-num2
    elif (operador==3):
        return num1*num2
    elif (operador==4):
        return num1/num2
    elif (operador==0):
        return 'programa encerrado'
    else:
        return 'essa opção não existe'
conta = 1
while (conta!=0):
    x = float(input('1º valor: '))
    y = float(input('2º valor: '))
    conta = int(input('selecione o número correspondente à operação desejada:\n1. soma\n2. subtração\n3. multiplicação\n4. divisão\n0. sair\n'))
    print(calculadora(x, y, conta))

