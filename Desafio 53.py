frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split() #separou a frase em uma lista de palavras
junto = ''.join(palavras) #juntou as palavras da lista ignorando os espaços entre elas
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
    #print(junto[letra-1])
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else: 
    print('A frase digitada não é um palíndromo!')
    
    
    
    
    
# EXPLICAÇÃO DO FOR C IN RANGE (COMO FAZER ELE CONTAR AS LETRAS AO CONTRÁRIO)
''' 
- "len(junto) + 1" para descorir a ultima letra; 
-  +1 pois ele ignora o último digito);
-  -1 pois o orimeiro número é 0, ele vai ser o último, então tem que ter um dígito antes de 0;
-  -1 pra ele contar "subtraindo" (de trás para frente).
'''

