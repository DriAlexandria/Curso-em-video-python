print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end='_')
print('FIM')