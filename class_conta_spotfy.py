class ContaSpotfy:
    contador = 0
    def __init__(self, nome, email, plano) -> None:
        self.nome = nome
        self.email = email
        self.plano = plano
        ContaSpotfy.contador += 1
    def imprimir_dados_conta(self) -> None:
        print('======DADOS CONTA======')
        print(f'Usuário: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Plano: {self.plano}\n')
            
conta1 = ContaSpotfy('Vitória', 'vitoriafernanda@gmail.com', 'Universitário')
conta2 = ContaSpotfy('Ricardo', 'ricardoporfirio@gmail.com', 'Duo')
conta3 = ContaSpotfy('Rebeca', 'alessiarebeca@gmail.com', 'Família')

conta1.imprimir_dados_conta()
conta2.imprimir_dados_conta()
conta3.imprimir_dados_conta()

print(f'Número de contas cadastradas: {ContaSpotfy.contador}')
