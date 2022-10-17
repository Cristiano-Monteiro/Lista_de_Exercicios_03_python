pedidos = [0, 0, 0, 0, 0, 0]
nome_pedidos = [
    'Cachorro Quente', 
    'Bauru Simples',
    'Bauru com ovo',
    'Hambúrguer',
    'Cheeseburguer',
    'Refrigerante'
]
preco_total = 0

while(True):
    print("""
    Especificação   === Código ===  Preço
    Cachorro Quente ===  100   === R$ 1,20
    Bauru Simples   ===  101   === R$ 1,30
    Bauru com ovo   ===  102   === R$ 1,50
    Hambúrguer      ===  103   === R$ 1,20
    Cheeseburguer   ===  104   === R$ 1,30
    Refrigerante    ===  105   === R$ 1,00
    """)

    while(True):
        item_pedido = int(input('Código do pedido: '))
        if(100 <= item_pedido <= 105):
            break

    while(True):        
        quantidade_pedido = int(input('Quantidade de itens: '))
        if(quantidade_pedido > 0):
            break

    if(item_pedido == 100):
        preco = 1.2
    elif(item_pedido == 101):
        preco = 1.3
    elif(item_pedido == 102):
        preco = 1.5
    elif(item_pedido == 103):
        preco = 1.2
    elif(item_pedido == 104):
        preco = 1.3
    elif(item_pedido == 105):
        preco = 1

    preco_por_item = preco * quantidade_pedido
    preco_total += preco_por_item

    indice_pedidos = item_pedido - 100
    pedidos[indice_pedidos] = preco_por_item

    while(True):
        pergunta = int(input('Deseja encerrar pedido? Sim [1]; Não[2]  '))
        if(pergunta == 1 or pergunta == 2):
            break
    
    if(pergunta == 1):
        break

print('___'*30)
print('# Valor pago por item:')
print()
for i in range(len(pedidos)):
    if(pedidos[i] != 0):
        print('===', nome_pedidos[i], '=== R$ %.2f' %pedidos[i])
print('___'*30)
print('# Preço Total dos pedidos: R$ %.2f' %preco_total)