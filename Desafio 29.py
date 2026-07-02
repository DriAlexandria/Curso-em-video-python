# multa por velocidade
velocidade = float(input('Qual é a velocidade atual do veículo? '))

if velocidade > 80:
    print("MULTADO! Vc excedeu o limite permitido que é de 80 km/h")
    multa = (velocidade - 80) * 7 #multiplica por 7 por que a multa custa 7 reais por km excedido
    print('Voce deve pagar uma multa de R${}!'.format(multa))

else:
    print('Tenha um bom dia, dirija com seguranca!')