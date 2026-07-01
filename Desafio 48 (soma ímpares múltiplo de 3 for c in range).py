soma=0
cont=0 #variável "Contador"
for c in range(1, 501, 2): #"2" pra mostrar apenas números ímpares (1,3,5...)
    if c % 3 == 0: #para mostrar apenas só números e múltiplos de 3 (3,6,9...)
        '''print(c, end=' ')''' #O enuncidado da questão não pede para mostrar todos os números na tela, mas no início é bom para conferir!
        cont = cont + 1 #operação para contar a quantidade de números (ímpares e divisíveis por 3) mostrados anteriormente
        soma = soma + c
print('A soma desses {} valores solicitados é igual a {}'.format(cont, soma))
