lista_classificacao = []

def classificacao_final(resultados):
    maior_media = 0

    for atleta in range(len(resultados)):
        print('___'*30)
        print('Atleta:', resultados[atleta][0])
        print('Saltos:', resultados[atleta][1])
        print('Melhor salto:', resultados[atleta][2])
        print('Pior salto:', resultados[atleta][3])
        print('Média dos demais saltos: %.2f' %resultados[atleta][4])
        if(resultados[atleta][4] > maior_media):
            maior_media = resultados[atleta][4]

    print('___'*30)
    print('RESULTADO FINAL:', maior_media)

while(True):
    lista_atleta = ['',0,0,0,0]
    saltos = []
    while(True):
        nome = str(input('Nome do Atleta[0 para sair]: '))
        if(nome.strip() != ''):
            break

    if(nome[0] in '0'): 
        break

    lista_atleta[0] = nome

    for i in range(0,5):
        salto = float(input('Salto: '))
        saltos.append(salto)

    lista_atleta[1] = saltos
    lista_atleta[2] = max(saltos)
    lista_atleta[3] = min(saltos)

    saltos_copia = saltos[::]

    for j in saltos_copia:
        if(j == max(saltos_copia) or j == min(saltos_copia)):
            saltos_copia.remove(j)
        
    media_saltos = sum(saltos_copia) / len(saltos_copia)

    lista_atleta[4] = media_saltos

    lista_classificacao.append(lista_atleta)

classificacao_final(lista_classificacao)