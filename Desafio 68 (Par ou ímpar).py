from random import randint
print('=-' *20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' *20)
vitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor de 0 a 10: '))
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print ('Você PERDEU!')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print ('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitorias} vezes!')