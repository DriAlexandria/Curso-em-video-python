num = cont = soma = 0
num = int(input('Digite um número [999 pra parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 pra parar]: ')) 
print('Você digitou {} número(s) e a soma entre eles é {}'.format(cont, soma))