# catetos e hipotenusa com biblioteca
import math
n1 = float(input('Cateto oposto: '))
n2 = float(input('Cateto adjacente: '))
hipotenusa = math.hypot(n1, n2)
print('A hipotenusa é igual a: {}'.format(hipotenusa))

