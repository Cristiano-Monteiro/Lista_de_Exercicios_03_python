from random import randint

nome_candidatos = ['João', 'Maria', 'Luiz', 'Paulo']
candidato_1 = candidato_2 = candidato_3 = candidato_4 = votos_nulos = votos_brancos = 0
total_votos_por_candidato = [0, 0, 0, 0]

total_votos = int(input('Quantidade de votos total: '))

for voto in range(0, total_votos):
    votos_eleitor = randint(1,6)
    if(votos_eleitor == 1):
        candidato_1 +=1
    elif(votos_eleitor == 2):
        candidato_2 += 1
    elif(votos_eleitor == 3):
        candidato_3 += 1
    elif(votos_eleitor == 4):
        candidato_4 += 1
    elif(votos_eleitor == 5):
        votos_nulos += 1
    elif(votos_eleitor == 6):
        votos_brancos += 1

total_votos_por_candidato[0] = candidato_1
total_votos_por_candidato[1] = candidato_2
total_votos_por_candidato[2] = candidato_3
total_votos_por_candidato[3] = candidato_4

porcentagem_votos_nulos = (votos_nulos / total_votos)*100
porcentagem_votos_branco = (votos_brancos / total_votos)*100

print('___'*30)
print('# O total de votos para cada candidato: ')
print()
for i in range(len(nome_candidatos)):
    print('===', nome_candidatos[i], '== Votos:', total_votos_por_candidato[i])
print('___'*30)
print('Total de votos nulos:', votos_nulos)
print('Total de votos em branco:', votos_brancos)
print('A percentagem de votos nulos sobre o total de votos: %.1f' %porcentagem_votos_nulos, '%')
print('A percentagem de votos em branco sobre o total de votos: %.1f' %porcentagem_votos_branco, '%')