#Simulador de caixa eletrônico
print('=' * 30)
print('{:^30}'.format('BANCO DEV'))
print('=' * 30)
#variáveis:
valor = int(input('Qual valor você quer sacar? R$'))
total = valor 
#a variável "total" existe para que a variável "valor" não seja alterada.
#o total será alterado toda vez que um valor de cédula for subtraído da variável "valor"
ced = 50 #essa é a cédula mais alta que tenho no caixa eletrônico.
totced = 0 #essa variável servirá para contar quantas cédulas serão precisas pra formar o "valor"

#começando o loop:
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else: #quando não der mais para tirar a cédula mais alta, temos que verficar qual a cédula atual (50, 20, 10 ou 1)
        if totced > 0:
            print(f'total de {totced} cédulas de R${ced}') #essa mensagem só vai aparecer quando der para tirar a cédula
        if ced == 50: #se não der mais pra tirar 50, o próximo valor q ele tentará é o de 20 
            ced = 20
        elif ced == 20:
            ced == 10
        elif ced == 10:
            ced = 1
        if total == 0: #a variável total foi alterada por causa das subtrações dos valores.
            break #se "total" for igual a 0, o caixa para de subtrair e mostrar as cédulas q vão ser scadas.
print('=' * 30)
print('VOLTE SEMPRE AO BANCO DEV')