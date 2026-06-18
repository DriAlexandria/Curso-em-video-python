from random import randint

print('''Sou o seu computador...
Acabei de pensar em um númeor de 0 a 10.
Será que você consegue adivinhar qual foi?''')

computador = randint(0, 10)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    
    if jogador < computador:
        print('Mais... Tente mais uma vez!')
    elif jogador > computador:
        print('Menos... Tente mais uma vez!')
    elif jogador == computador:
        acertou = True
    
print('Você ACERTOU!!! E usando apenas {} palpite(s)!'.format(palpites))
    
    
    
    
