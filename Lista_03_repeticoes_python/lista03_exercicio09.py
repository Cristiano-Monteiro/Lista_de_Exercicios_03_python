lista_tipos_defeito = []

print("""
--------------------------------------------------
# Nº de identificação do tipo de defeito no mouse:
1- necessita da esfera 
2- necessita de limpeza 
3- necessita troca do cabo ou conector
4- quebrado ou inutilizado
--------------------------------------------------""")

while(True):
    while(True):
        defeito = int(input('Tipo de defeito no mouse[0 para encerrar]: '))
        print('---'*30)
        if(0 <= defeito <= 4):
            break
    if(defeito == 0):
        break
    lista_tipos_defeito.append(defeito)

defeito1 = 0
defeito2 = 0
defeito3 = 0
defeito4 = 0

for defeito in lista_tipos_defeito:
    if(defeito == 1):
        defeito1 += 1
    elif(defeito == 2):
        defeito2 += 1
    elif(defeito == 3):
        defeito3 += 1
    else:
        defeito4 += 1

total_mouses = defeito1 + defeito2 + defeito3 + defeito4
print('Quantidade de mouses:', total_mouses)
print("""
    Situação--------------------------------------Quantidade----------------------------Percentual
    ----------------------------------------------------------------------------------------------
    1- necessita da esfera--------------------------- {} ---------------------------------- {:.0f}% 
    2- necessita de limpeza-------------------------- {} ---------------------------------- {:.0f}% 
    3- necessita troca do cabo ou conector----------- {} ---------------------------------- {:.0f}% 
    4- quebrado ou inutilizado ---------------------- {} ---------------------------------- {:.0f}% 
""".format(defeito1, (defeito1/total_mouses)*100, defeito2, (defeito2/total_mouses)*100, defeito3, (defeito3/total_mouses)*100, defeito4, (defeito4/total_mouses)*100))
