#COMO USAR LAÇO (para repetir algo várias vezes)
for c in range (0, 6): #laço contador no intervalo de 1 a 6
    print('Oi') #Vai mostrar "oi" 6 vezes
print('Fim')

for c in range (0, 6): 
    print(c) #Vai contar de 1 a 5 (o último número ele ignora)
print('Fim')

for c in range (6, 0, -1): #Para contar de trás pra frente precisa do "-1" (interação: ele vai começar do 6 e vai subtraindo 1)
    print(c) #Vai contar do 6 ao 1
print('Fim')

for c in range (0, 7, 2): #Nesse exemplo o "2" é a interação. 
    print(c) #Ele vai contar de 0 a 6 pulando de 2 em dois: 0, 2, 4, 6.
print('Fim')

#MAIS EXEMPLOS
#1
n = int(input('Digite um número: '))
for c in range(0, n+1): #se o número digitado for 7, ele só conta até 6. Pra que ele conte até 7, coloque o "+1"
    print(c)
print('FIM')

#2
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): #"Começa pelo número digitado em 'Início', vai até o número do 'fim' + 1 e vai pulando de passo em passo"
    print(c)
print('FIM')

#3
for c in range(0, 3):
    n= int(input('Digite um número: ')) #Esse comando para digitar está dentro de um "for" que conta de 0 a 3. 
print('FIM')                            #Então esse comand será repetido 3 vezes

#4
s=0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('O somatório de todos os valores foi {}'.format(s))

