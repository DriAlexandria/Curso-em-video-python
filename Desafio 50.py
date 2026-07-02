# soma de pares for c in range
s=0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s = s + num 
        cont = cont + 1 
print('Você me informou {} números PARES e a soma desses números é igual a {}'.format(cont, s))
