nome = ''
anoNasc = 0
dados = False
while (dados==False):
    try:
        nome = input('NOME: ')
        anoNasc = int(input('ANO DE NASCIMENTO: '))
        if (anoNasc >1992 and anoNasc < 2021):
            idade = 2022-anoNasc
            dados = True
            print(f'NOME: {nome}\nCOMPLETA/COMPLETARÁ {idade} ANOS')
        elif (anoNasc < 1992 or anoNasc > 2021):
            raise Exception ('ano deve estar entre 1992 e 2021')
        elif (type(anoNasc) != int):
            raise Exception ('caracter inválido')
    except Exception as err:
        print(err)
