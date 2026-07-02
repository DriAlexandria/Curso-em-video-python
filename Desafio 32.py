# ano bissexto
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual! '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 400 == 0:
    print ('O ano {} é BISSEXTO!'.format(ano))
else:
    print ('O ano {} NAO é BISSEXTO!'.format(ano))





#Explicando o cálculo do ano bissexto: 
    #Ser divisível por 4 (ex: 2024, 2028, 2032).
    #Se terminar em "00", só é bissexto se também for divisível por 400