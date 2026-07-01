#INTERROMPENDO REPETIÇÕES WHILE
'''esse recurso é usado quando não ha condição de parada (ex: while true), fazendo o loop infinitamente'''
#exemplo lúdico português:
'''enquanto VERDADEIRO: 
    se tiver chão:
        passo
    se tiver buraco:
        pula
    se tiver moeda:
        pega
    se tiver troféu:
        pula
        INTERROMPA 
pega'''
#Exemplo lúdico com comandos (inglês):
'''while True: 
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
    if troféu:
        pula
        break 
pega'''

#RECAPTULANDO WHILE COM CONDIÇÃO DE PARADA:
#1 - (nesse exemplo ele vai mostrar os números até chegar a 10 que é a condição de parada)
cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

#2 - (nesse exemplo você vai digitar números infinitamente e só vai parar quando vc digitar 999.)
#(Só que na parte da soma, ele vai acabar somando o 999)
n = 0
s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}.'.format(s))

#3 - para a soma não incluir a condição de parada o código deve ficar assim:
n = 0
s = 0
while True: #sem condição de parada = looping infinito
    n = int(input('Digite um número: '))
    if n == 999:
        break #interromper quando digitar 999
    s += n
print('A soma vale {}.'.format(s))

#4 - exemplo usando "f-strings" 
# Coloca-se um f na frente do texto que quer exibir. 
# Ele substitui o format colocado no final pois vc pode colocar o nome da variável dentro das {}.
nome = 'José'
idade = 33
salario = 987.3
print(f'{nome} tem {idade} e recebe R${salario}')

