# jogo da adivinhação
from random import randint
from time import sleep #faz o computador dormir

computador = randint(0, 5) #faz o computador "Pensar" em um número aleatório inteiro
print('Vou pensar em um númeor entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2) #espera 2 segundos antes de mostrar a resposta

if jogador == computador:
    print('PARABÉNS! Vc venceu!')
else:
    print('Perdeu! Eu pensei no número {} e não no número {}!'.format(computador, jogador))