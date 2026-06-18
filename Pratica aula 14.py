#COMO USAR WILE: 
#exemplo lúdico português:
'''enquanto não tiver a maçã:
    se tiver chão:
        passo
    se tiver buraco:
        pula
    se tiver moeda:
        pega
pega'''
#Exemplo lúdico com comandos (inglês):
'''while not maçã:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega'''

#PRÁTICA:
#"Quando sabemos o limite":
'''for c in range (1, 10):
    print(c)
print('Fim')

é igual a:'''

c=1
while c< 10:
    print(c)
    c = c + 1
print('Fim')

#Quando não sabemos o limite:
n=1
while n != 0: #Enquanto o valor 0 não for digitado, o programa não irá parar de pedir um valor
    n= int(input('Digite um valor: ')) #não se sabe quantas vezes ele irá pedir
print('Fim')

    #outra situaçao (laço indeterminadas vezes):
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')

#outro exemplo:
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: #O 0 vai ser digitado para parar o laço, e esse if servirá para ele não analisar o 0 como par ou impar
        if n % 2 == 0:
            par += 1 #vai contar quantos foram pares
        else:
            impar += 1 #vai contar quantos foram ímpares
print('Você digitou {} número(s) par(es) e {} número(s) ímpar(es)!'.format(par, impar))