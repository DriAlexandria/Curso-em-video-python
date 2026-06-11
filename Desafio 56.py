soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulher_20 = 0
for p in range(1, 5):
    print('-----{}º PESSOA -----: '.format(p))
    
    #DADOS
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    
    #MEDIA IDADE GRUPO
    soma_idade += idade
    media_idade = soma_idade/4
    
    #NOME DO HOMEM MAIS VELHO
    if p == 1 and sexo in 'M m':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'M m' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    #QUANTAS MULHERES TEM - 20 ANOS
    if sexo in 'F f' and idade < 20:
        mulher_20 += 1
print('A média de idade do grupo é {}'.format(media_idade))
print('O homem mais velho tem {} ano(s) e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo, {} mulher(es) tem menos de 20 anos!'.format(mulher_20))
    
    
    
    
    
    
