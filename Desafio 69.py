# Cadastrando pessoas..
maioridade = 0
homens = 0
mulher_20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    
    #cadastrando idade
    idade = int(input('Idade: '))
    
    #cadastrando sexo
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    
    #condições:
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    
    #perguntando se quer continuar
    resp = ' '
    while resp not in 'SN': 
        print('-' * 30)
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Ao todo {maioridade} pessoas são maiores de 18.')
print(f'{homens} homens foram cadastrados.')
print(f'E {mulher_20} mulheres tem menos de 20 anos')