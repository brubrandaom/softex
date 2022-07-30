nome = ''
anoNasc = 0
dados = False
def function (nome, dados, anoNasc):
    while (dados==False):
        nome = input('NOME: ')
        anoNasc = int(input('ANO DE NASCIMENTO: '))
        if (anoNasc >1992 and anoNasc < 2021):
            idade = 2022-anoNasc
            dados = True
        elif (anoNasc < 1992 or anoNasc > 2021):
            raise Exception ('ano deve estar entre 1992 e 2021')
        else:
            raise Exception ('caracter inválido')
    return idade, nome

try:
    idade, nome = function(nome, dados, anoNasc)
    print(f'NOME: {nome}\nCOMPLETA/COMPLETARÁ {idade} ANOS')
except Exception as err:
    print(err)
