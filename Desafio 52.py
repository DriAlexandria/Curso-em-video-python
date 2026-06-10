num = int(input('Digite um número: '))
total = 0 #variável para contar o tanto de números pelos quais o num foi divisível
for c in range(1, num + 1): #vai contar do 1 até o número que vc digitou
    if num % c == 0: #se o num digitado for divisível pelos números contados até chegar nele...
        print('\033[33m', end= ' ') #os números pelos quais ele for divisível vai ficar na cor amarelo
        total += 1 #total = total + 1
    else:
        print('\033[31m', end= ' ') #os némros pelos quais ele n é divisível vai ficar vermelho
    print('{}'.format(c), end= '\033[m') #vai mostrar essa contagem; \033[m para a cor parar de aparecer no resto do texto
print('\n O número {} foi divisível por {} número(s)!'.format(num, total)) #\n para qubrar a linha
if total == 2: #2 POR QUE SE ELE FOR PRIMO, SÓ VAI SER DIVISÍVEL DUAS VEZES (POR 1 E POR ELE MESMO.)
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é primo!')