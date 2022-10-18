def calculo_consumo(consumo_carros):
    resultado_consumo = []
    for cons in consumo_carros:
        resultado = 1000/cons
        resultado_consumo.append(resultado)
    return resultado_consumo

def custo_consumo(lista_consumo):
    resultado_custo = []
    for cons in lista_consumo:
        custo = 2.25 * cons
        resultado_custo.append(custo)
    return resultado_custo

modelos_carros = []
consumo_carros = []

print('==='*40)
print('Comparativo de Consumo de Combustível:')
for cont in range(0, 5):
    modelo = str(input('Modelo do carro: '))
    consumo = float(input('Consumo do carro[Km/L]: '))
    modelos_carros.append(modelo)
    consumo_carros.append(consumo)
print('==='*40)

lista_resultado_consumo = calculo_consumo(consumo_carros)
lista_custo_consumo = custo_consumo(lista_resultado_consumo)

print('Relatório Final:')
print('==='*40)
for i in range(0, 5):
    print('{} -- {} ---- {} Km/L ---- {:.1f} Litros -- R$ {:.2f}'.format(i+1, modelos_carros[i], consumo_carros[i], lista_resultado_consumo[i], lista_custo_consumo[i]))
print('==='*40)
for j in range(len(lista_resultado_consumo)):
    if(lista_resultado_consumo[j] == min(lista_resultado_consumo)):
        print('O menor consumo é do {}.'.format(modelos_carros[j]))