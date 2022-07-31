fimVotacao = 'n'
votosX = 0
votosY = 0
votosZ = 0
votosNulo = 0

while (fimVotacao == 'n'):
    try:
        voto = int(input('=== ESCOLHA UM CANDIDATO ===\nX => 889\nY => 847\nZ => 515\nBranco => 0\n'))
        if (voto == 889):
            votosX+=1
        elif (voto == 847):
            votosY+=1
        elif (voto == 515):
            votosZ+=1
        else:
            votosNulo+=1
        fimVotacao = input('Deseja finalizar a votação? [s/n]\n')
    except:
        print('\nERRO, tente novamente\n')
        fimVotacao = 'n'
        
if (votosX > votosY and votosX > votosZ):
    print('\nVENCEDOR: Candidato X\n')
elif (votosY > votosX and votosY > votosZ):
    print('\nVENCEDOR: Candidato Y\n')
elif (votosZ > votosX and votosZ > votosY):
    print('\nVENCEDOR: Candidato Z\n')
elif (votosX == votosY):
    print('\nCandidatos X e Y empataram em número de votos\n')
elif (votosX == votosZ):
    print('\nCandidatos X e Z empataram em número de votos\n')
elif (votosY == votosZ):
    print('\nCandidatos Y e Z empataram em número de votos\n')
else:
    print ('\nHouve empate entre todos os candidaros\n')
        
print (f'=== RSULTADOS ===\nCandidato X: {votosX} votos\nCandidato Y: {votosY} votos\nCanditato Z: {votosZ} votos\nBranco/Nulo: {votosNulo} votos')
