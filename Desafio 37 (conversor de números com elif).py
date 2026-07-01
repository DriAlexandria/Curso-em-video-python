num = int(input('Digite um número: '))
print('''Agora escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opçao = int(input("Digite o número da opção escolhida: "))
if opçao == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif opçao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif opçao == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Opção INVÁLIDA! Tente novamente!')

