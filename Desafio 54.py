from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nesceu?: '.format(c)))
    idade = atual - nasc
    if idade <= 18:
        maior += 1
    else:
        menor += 1
print ("Ao todo tivemos {} pessoa(s) maior de idade e {} pessoa(s) menor de idade".format(maior, menor))
    