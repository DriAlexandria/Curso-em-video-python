# pagamento na loja com elif
print('{:=^40}'.format(' LOJA ALEXANDRIA '))

preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Opção escolhida: '))
if opçao == 1:
    total = preço - (preço * 0.10) #total == preço com desconto de 10%
elif opçao == 2:
    total = preço - (preço * 0.05) #total == preço com desconto de 5%
elif opçao == 3:
    total = preço #não houve desconto então o total == preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 0.20) #total == preço com + 20% de juros
    vezes = int(input('Quantas parcelas? '))
    parcela = total / vezes
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(vezes, parcela))
else:
    print('Opção INVÁLIDA de pagamento! Por favor digite novamente!')
    exit()
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
    
