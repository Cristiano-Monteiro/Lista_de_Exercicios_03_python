from random import randint

intervalo1 = intervalo2 = intervalo3 = intervalo4 = total_num = 0

while(True):
    num = randint(-1,100)
    if(num < 0):
        break
    total_num += 1
    if(0 <= num <= 25):
        intervalo1 += 1
    elif(26 <= num <= 50):
        intervalo2 += 1
    elif(51 <= num <= 75):
        intervalo3 += 1
    elif(76 <= num <= 100):
        intervalo4 += 1

print('# Quantidade total de números:', total_num)
print('=== Intervalo [0-25]:', intervalo1)
print('=== Intervalo [26-50]:', intervalo2)
print('=== Intervalo [51-75]:', intervalo3)
print('=== Intervalo [76-100]:', intervalo4)