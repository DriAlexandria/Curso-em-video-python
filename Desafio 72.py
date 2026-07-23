numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num_digitado = int(input('Digite um número de 0 a 20: '))
    if 0 <= num_digitado <= 20:
        print(f'Você digitou o número {numeros[num_digitado]}!')
        resp = ' '
        while resp not in 'SN': 
            print('-' * 30)
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            print('-' * 30)
        if resp == 'N':
            break
    else:
        print('Número inválido, tente novamente!')
