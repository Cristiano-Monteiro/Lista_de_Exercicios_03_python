# O arquivo "usuarios.txt" é necessário para o funcionamento do programa.

def conversao_bytes_megabytes(lista_espaco_ocupado):
    espaco_em_MB = []
    for espaco in lista_espaco_ocupado:
        conversao = int(espaco) / (1024)**2
        espaco_em_MB.append(conversao)
    return espaco_em_MB

def calculo_percentual(lista_espacos, espaco_total):
    resultado = []
    for espaco in lista_espacos:
        calculo = (espaco / espaco_total)*100
        resultado.append(calculo)
    return resultado

with open('usuarios.txt', 'r') as arquivo:
    lista_usuarios = arquivo.readlines()

lista_nomes = []
lista_espaco_ocupado = []

for usuario in lista_usuarios:
    user = usuario.split()
    lista_nomes.append(user[0])
    lista_espaco_ocupado.append(user[1])

lista_espaco_convertido_MB = conversao_bytes_megabytes(lista_espaco_ocupado)

espaco_total = sum(lista_espaco_convertido_MB)
espaco_medio = espaco_total / len(lista_espaco_convertido_MB)
percentual_espaco = calculo_percentual(lista_espaco_convertido_MB, espaco_total)

with open('relatório.txt', 'w') as arquivo:
    arquivo.write('ACME Inc. Uso do espaço em disco pelos usuários\n')
    arquivo.write('------------------------------------------------------------------------\n')
    arquivo.write("Nr.  Usuário      Espaço utilizado      % do uso\n")
    for i in range(len(lista_nomes)):
        arquivo.write('{}   {:9}      {:9.2f}  MB        {:6.2f}%\n'.format(i+1 ,lista_nomes[i], lista_espaco_convertido_MB[i], percentual_espaco[i]))
    arquivo.write('------------------------------------------------------------------------\n')
    arquivo.write('Espaço total ocupado: {:.2f} MB\n'.format(espaco_total))
    arquivo.write('Espaço médio ocupado: {:.2f} MB'.format(espaco_medio))