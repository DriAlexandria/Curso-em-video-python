frase = input('Digite uma frase: ')
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[c]

print(inverso)

if inverso == frase:
    print("Temos um palindromo")
else:
    print("A frase n é palindromo")