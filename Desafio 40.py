# média nota com elif
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2)/2
print('Quem tirou {:.1f} e {:.1f} tem a média de {:.1f}.'.format(nota1, nota2, media))
if media >= 7:
    print('O aluno está APROVADO!')
elif 7 > media >= 5:
    print('O aluno está de RECUPERAÇÃO!')
elif media < 5:
    print('O aluno está REPROVADO')
