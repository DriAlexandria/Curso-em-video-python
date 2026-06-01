#EXPLICAÇÃO:
'''\033[style;text;backm]

style: estilo da fonte(normal, negrito, sublinhada...)
    0 - nada
    1 - negrito (bold)
    4 - Sublinhado (Underline)
    7 - Inverte as config (Negativo = "O que vc colocou pra letra vai pro fundo e vice/versa)
text: cor do texto
    30 ao 37 na ordem: (branco, verm, verde, amarelo, azul, roxo, ciano, cinza)
back: cor do fundo
    40 ao 47 na ordem: (branco, verm, verde, amarelo, azul, roxo, ciano, cinza)
'''

#EXEMPLO:
print('\033[1;31;43m Olá mundo! \033[m') #(Letra em negrito vermelha com fundo amarelo)
print('\033[4;30;45m Olá mundo! \033[m') #(Letra sublinhada branca com fundo roxo)
print('\033[7;30m Olá mundo! \033[m') #(letra preta, fundo branco)
#obs: terminar o print com \033[m faz com que a cor do fundo vá somente até o fim da frase.

#PRIMEIRA FORMA DE FAZER (no print):
a=3
b=5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))

#SEGUNDA FORMA DE FAZER (usando o .format):
nome = 'Drielly'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m')) 
#obs: {Cód.cor abrindo}{Veriável}{Cód. cor fechando}

#TERCEIRA FORMA DE FAZER (usando variável):
nome= "Drielly"
cores= {'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7;30m'}
print('Olá, muito prazer em te conhecer,{}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
