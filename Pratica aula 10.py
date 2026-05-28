nome=str(input('Qual é o seu nome? ')).strip().capitalize()
if nome == 'Drielly':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome é tao normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Primeira nota:  '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {}.'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

