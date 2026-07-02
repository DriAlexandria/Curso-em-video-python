# sen, cos, tan, com biblioteca
import math
n = float(input('Digite um angulo: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('O seno é igual a: {:.2f}'.format(s))
print('O Cosseno é igual a: {:.2f}'.format(c))
print('A tangente é igual a: {:.2f}'.format(t))
