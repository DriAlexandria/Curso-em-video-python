#TUPLAS (VARIÁREIS COMPOSTAS)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2]) #pizza
print(lanche[2:]) #pizza, pudim (do 2 até o final)
print(lanche[:2]) #hamburguer, suco (do início até o 2 ignorando o 2 (phyton ignora o último))
print(lanche[-2]) #pizza (contando de trás para frente (pudim = -1, pizza = -2...))
print(lanche[-3:]) #suco, pizza, pudim (conta do -3 até o final (-1))

#TUPLAS SÃO IMUTÁVEIS = não da pra mudar os elementos de uma tupla
#ex:
lanche[1] = 'refrigerante' #ERRO "os objetos da tupla não podem ter itens atribídos"

#TUPLAS NO "FOR C IN RANGE":
#1
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}') #aqui ele irá mostrar essa frase com cada comida presente na tupla na ordem
print('Comi pra caramba!')

#2 - nesse modo não precisa de uma frase para mostrar os nomes das comidas
for cont in range(0, len(lanche)):
    print(cont) #mostrará só os números correspondentes a cada comida
    print(lanche[cont]) #mostrará apenas os nomes das comidas na ordem dos números (0, 1, 2....)
print('Comi pra caramba!')

#3 - se precisar mostrar a posição da comida na tupla:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #"vou comer pudim na posição 3"

'''ou'''
for pos, comida in enumerate(lanche): #pos = posição; enumerate = enumerar as posições
    print(f'Eu vou comer {comida} na posicção {pos}')
    
#PARA ORGANIZAR:
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche)) #para organizar as palavras em ordem alfabética

#MAIS EXEMPLOS:
#1:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #a ordem que vc soma as tuplas interefere no resultado
print(c) #junta as duas ao invés de somar os números (ex: 2, 5, 4, 5, 8, 1, 2) 
print(len(c)) #vai mostrar o tanto de dígitos que tem na tupla (ex: 7)
print(c.count(5)) #mostra quantas vezes aparece o núm 5 dentro de c (ex: 2)
print(c.index(8)) #mostra a posicação em que o num 8 aparece (ex: 1º posição) considerando 0 como a primeira e pegando apenas a primeira vez que ele aprece
print(c.index(5, 1)) #mostra a posição da primeira ocorrência do num 5 a partir da primeira posição (ex: 5º posição)

#APAGANDO UMA VARIAVEL:
pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
#esse comando serve para deletar a tupla inteira
#não dá para apagar apenas um elemento da tupla
