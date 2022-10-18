lista_classificacao = []

def classificacao_final(resultados):
    maior_media = 0
    melhor_atleta = 0

    for atleta in range(len(resultados)):
        print('___'*30)
        print('Atleta:', resultados[atleta][0])
        print('Notas:', resultados[atleta][1])
        print('Média: %.2f' %resultados[atleta][4])
        if(resultados[atleta][4] > maior_media):
            maior_media = resultados[atleta][4]
            melhor_atleta = resultados[atleta]

    print('___'*30)
    print('RESULTADO FINAL:')
    print('Atleta:', melhor_atleta[0])
    print('Notas:', melhor_atleta[1])
    print('Melhor nota:', melhor_atleta[2])
    print('Pior nota:', melhor_atleta[3])
    print('Média: %.2f' %melhor_atleta[4])

while(True):
    lista_atleta = ['',0,0,0,0]
    notas = []
    while(True):
        nome = str(input('Nome do Atleta[0 para sair]: '))
        if(nome.strip() != ''):
            break

    if(nome[0] in '0'): 
        break

    lista_atleta[0] = nome

    for i in range(0,7):
        nota = float(input('Nota: '))
        notas.append(nota)

    lista_atleta[1] = notas
    lista_atleta[2] = max(notas)
    lista_atleta[3] = min(notas)

    notas_copia = notas[::]

    for j in notas_copia:
        if(j == max(notas_copia) or j == min(notas_copia)):
            notas_copia.remove(j)
        
    media_notas = sum(notas_copia) / len(notas_copia)

    lista_atleta[4] = media_notas

    lista_classificacao.append(lista_atleta)

classificacao_final(lista_classificacao)