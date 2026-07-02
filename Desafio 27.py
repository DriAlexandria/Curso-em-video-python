# primeiro e último nome
n = str(input('Digite o seu nome completo: ')).strip().upper()
nome  = n.split()
print('Primeiro Nome: {}'.format(nome[0]))
print('Último Nome: {}'.format(nome[len(nome)-1]))