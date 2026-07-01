#RESOLUCAO 1

'''km = float(input('Qual é a distancia da sua viagem?: '))
if km <= 200: #viagem curta
    preco1 = km * 0.50 #preco normal
    print("O preco da sua passagem será de R${:.2f}".format(preco1))
else: #viagem longa
    preco2 = km * 0.45 #preco promocional
    print('O preco da sua passagem será de R${:.2f}'.format(preco2))'''

#RESOLUCAO SIMPLIFICADA

km = float(input('Qual é a distancia da sua viagem?: '))
preco = km * 0.50 if km <= 200 else km * 0.45
print('O preco da sua passagem será de R${:.2f}'.format(preco))