casa = float(input('Qual o valor da casa?: R$'))
salario = float(input('Qual o salário do comprador?: R$'))
anos = int(input('Em quantos anos deseja pagar?: '))
parcela = casa / (anos * 12)
minimo = salario * 0.3
print('Para pagar uma casa no valor de {:.2f} em {} anos, o valor da sua parcela será de R$ {:.2f}'.format(casa, anos, parcela))
if parcela <= minimo:
    print('PARABÉNS!! Seu empréstimo foi CONCEDIDO!')
else:
    print('Que pena!! Seu empréstimo foi NEGADO!')