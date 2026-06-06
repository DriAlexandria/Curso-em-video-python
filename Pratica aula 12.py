#ESTRUTURA CONDICIONAL ANINHADA
nome = str(input('Qual é o seu nome? ')).capitalize()
if nome == 'Drielly':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}'.format(nome))

'''
OBS: Posso usar eliff quantas vezes eu quiser;
O uso do else não é obrigatório quando se tem o elif.
'''