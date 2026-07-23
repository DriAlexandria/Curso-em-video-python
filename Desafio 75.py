#TUPLA COM INPUt
valores = (int(input('Digite um valor:')), int(input('Digite um valor:')), 
        int(input('Digite um valor:')), int(input('Digite um valor:')))
print(f'Você digitou os valores {valores}.')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 apareceu na {valores.index(3) + 1}º posição.')