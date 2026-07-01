from random import randint
from time import sleep #faz o computador dormir
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: #pedra
    if jogador == 0:
        print('Deu Empate')
    elif jogador == 1: 
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada Inválida')
        
elif computador == 1: #papel
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1: 
        print('Deu Empate')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Inválida')
elif computador == 2: #tesoura
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1: 
        print('Computador Venceu')
    elif jogador == 2:
        print('Deu Empate')
    else:
        print('Jogada Inválida')