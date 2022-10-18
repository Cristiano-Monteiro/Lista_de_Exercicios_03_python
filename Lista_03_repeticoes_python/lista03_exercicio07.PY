def calculo_abono(tot_salarios):
    lista_com_abonos = []
    for salario in tot_salarios:
        calculo = 0.2 * salario
        if(calculo < 100):
            calculo = 100
        lista_com_abonos.append(calculo)
    return lista_com_abonos

total_salarios = []

while(True):
    salario = float(input('Digite o salário[0 para finalizar]: R$ '))
    if(salario == 0):
        break
    total_salarios.append(salario)

resultado_abono = calculo_abono(total_salarios)

print('==='*30)
print('Projeção de Gastos com Abono:')
for slr in total_salarios:
    print('Salário:         R$ {:.2f}'.format(slr))
print('==='*30)
for i in range(len(total_salarios)):
    print('Salário: R$ {:.2f} -------- Abono: R$ {:.2f}'.format(total_salarios[i], resultado_abono[i]))
print('==='*30)
print('Foram processados {} colaboradores.'.format(len(total_salarios)))
print('Total gasto com abonos: R$ {:.2f}'.format(sum(resultado_abono)))
quantidade_valor_minimo = 0
for j in resultado_abono:
    if(j == 100):
        quantidade_valor_minimo += 1
print('Valor mínimo pago a {} colaboradores.'.format(quantidade_valor_minimo))
print('Maior valor de abono pago: R$ {:.2f}'.format(max(resultado_abono)))