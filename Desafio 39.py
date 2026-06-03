from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu nao de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o seu alistamento!'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você ja passou dos 18, deveria ter se alistado a {} anos.'.format(saldo))