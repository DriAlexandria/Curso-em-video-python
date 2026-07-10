#Loja com While e Break
print('-' * 30)
print('SUPER BERNARDÃO')
print('-' * 30)
total = 0
quant = 0
#variáveis para o nome do produto com menor preço 
cont = 0
menor_preco = 0
nome_produto_menor = ''
while True:
    
    #Cadastrando Produto:
    nome_produto = str(input("Nome do produto: "))
    
    #cadastrando o preço do produto:
    preco = float(input("Preço: "))
    cont += 1
    #somando os preços para dar o total:
    total += preco
    
    #condição para o preço maior que 1000:
    if preco > 1000:
        quant += 1
    
    #Condição para o menor preço:
    if cont == 1:
        menor_preco = preco
        nome_produto_menor = nome_produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_produto_menor = nome_produto
    
    #Perguntando se quer continuar:
    resp = ' '
    while resp not in 'SN': 
        print('-' * 30)
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 30)
    if resp == 'N':
        break
    
    #Frases finais:
print('====== FIM DO PROGRAMA ======')
print(f'O total da compra foi R${total}')
print(f'Temos {quant} produto(s) custando mais de R$1000')
print(f'O produto mais barato foi {nome_produto_menor} que custou {menor_preco:.2f}')

