#SOLUÇÃO UTILIZANDO A BIBLIOTECA
'''
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
'''

#SOLUÇÃO COM WHILE
n = int(input('Digite um número para calcular seu fatorial: '))
cont = n #o fatorial começa sempre com o númeoro que a pessoa vai sigitar
f = 1 #sempre que for trabalhar com  multiplicação, começa com 1.
print('Calculanodo {}! = '.format(n), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))