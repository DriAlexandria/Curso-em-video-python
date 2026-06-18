from time import sleep
#ESTOQUE
farinha = int(input('Quantos sacos de farinha existem no estoque? '))
molho = int(input('Quantos molhos de tomate existem no estoque? '))
oregano = int(input('Quantos pacotes de orégano existem no estoque? '))
queijo = int(input('Quantos queijos mussarela existem no estoque? '))
calabresa =  int(input('Quantas calabresas existem no estoque? '))
frango = int(input('Quantos frangos existem no estoque? '))
print('=-=' * 15)
#ATENDIMENTOS
max_pedidos = int(input('Qauntos atendimentos serão realizados hoje? '))
pedido = 1
print('=-=' * 15)

#ÁREA DO CLIENTE
while pedido <= max_pedidos:

    print('----- FAÇA O SEU PEDIDO -----')
    print('''    Atendimento número {}.
    Seja Bem-Vindo à pizzaria Erick's!!!'''.format(pedido))
    print('---------    MENÚ   ---------')
    print('''    [ 1 ] Pizza Mussarela
    [ 2 ] Pizza Calabresa
    [ 3 ] Pizza Frango''')
    print('-' * 30)
    opçao = int(input('>>>>> Qual sabor você deseja? '))
    pedido += 1   
#CONDIÇÕES PARA PODER PEDIR CADA PIZZA
    if opçao == 1:
        if farinha == 0 or molho == 0 or oregano == 0 or queijo == 0:
            sleep(1)
            print('Ingredientes em falta! Por favor escolha outro sabor!')
        else:
            farinha -= 1
            molho -= 1
            oregano -= 1
            queijo -= 1
            sleep(1)
            print ('Opa! Seu pedido é uma ordem e sairá em alguns minutos!')
    elif opçao == 2:
        if farinha == 0 or molho == 0 or oregano == 0 or calabresa == 0:
            sleep(1)
            print('Ingredientes em falta! Por favor escolha outro sabor!')
        else:
            farinha -= 1
            molho -= 1
            oregano -= 1
            calabresa -= 1
            sleep(1)
            print ('Opa! Seu pedido é uma ordem e sairá em alguns minutos!')
    elif opçao == 3:
        if farinha == 0 or molho == 0 or oregano == 0 or frango == 0:
            sleep(1)
            print('Ingredientes em falta! Por favor escolha outro sabor!')
        else:
            farinha -= 1
            molho -= 1
            oregano -= 1
            frango -= 1
            sleep(1)
            print ('Opa! Seu pedido é uma ordem e sairá em alguns minutos!')
#TIRANDO DO ESTOQUE A CADA ATENDIMENTO
    sleep(2)
    print('''    AINDA EM ESTOQUE: 
    {} saco (s) de farinha(s) 
    {} molho(s) de tomate
    {} pacote(s) de orégano
    {} queijo(s) mussarela
    {} calabresa(s)
    {} frango(s)'''.format(farinha, molho, oregano, queijo, calabresa, frango))
    print('=-=' * 15)
print('--------- FIM DOS ATENDIMENTOS --------')