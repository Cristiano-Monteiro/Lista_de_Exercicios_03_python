gabarito_prova = ['A','B','C','D','E','E','D','C','B']

lista_acertos = []

total_alunos = 0

def comparando_gabarito(lista_respostas):
    acertos = 0
    for i in range(len(gabarito_prova)):
        if(lista_respostas[i] == gabarito_prova[i]):
            acertos += 1
    lista_acertos.append(acertos)


while(True):
    total_alunos += 1
    respostas_prova = []
    for resp in range(1,11):
        while(True):
            print('Questão', resp, ': ', end='')
            resposta = str(input('')).upper()
            if(resposta in 'ABCDE'):
                break
        respostas_prova.append(resposta)
    
    comparando_gabarito(respostas_prova)

    while(True):
        pergunta = int(input('Outro aluno vai utilizar o sistema? Sim[1] ou Não[2] '))
        if(pergunta == 1 or pergunta == 2):
            break
    
    if(pergunta == 2):
        break

media_turma = sum(lista_acertos) / total_alunos

print('___'*30)
print('Maior Acerto:', max(lista_acertos))
print('Menor Acerto:', min(lista_acertos))
print('Total de Alunos que utilizaram o sistema:', total_alunos)
print('Média das Notas da Turma: %.1f' %media_turma)