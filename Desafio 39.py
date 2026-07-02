# Alistamento militar com elif
from datetime import date
atual = date.today().year
gen = str(input('Qual o seu gênero? ')).capitalize()
if gen in 'Feminino Mulher':
    print('Você não precisa fazer o alistamento militar!')
else:
    nasc = int(input('Qual o seu ano de nascimento? '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos, ainda falta(m) {} ano(s) para o seu alistamento!'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você ja passou dos 18, deveria ter se alistado a {} ano(s).'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))