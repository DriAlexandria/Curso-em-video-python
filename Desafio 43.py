# IMC com elif
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Esta pessoa está ABAIXO DO PESO!')
elif imc <= 25:
    print('Esta pessoa está com o PESO IDEAL!')
elif imc <= 30:
    print('Esta pessoa está com SOBREPRESO!')
elif imc <= 40:
    print('Esta pessoa está com OBESIDADE!')
elif imc > 40:
    print('Esta pessoa está com OBESIDADE MÓRBIDA!')

