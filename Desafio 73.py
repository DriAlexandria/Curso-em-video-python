times = ("Palmeiras", "Flamengo", "Fluminense", "Red Bull Bragantino", "Athletico Paranaense",
    "Bahia", "Coritiba", "São Paulo", "Botafogo", "Vitória",
    "Atlético Mineiro", "Corinthians", "Cruzeiro", "Internacional", "Santos",
    "Grêmio", "Vasco da Gama", "Mirassol", "Remo", "Chapecoense")
print('-=' * 30)
print(f'Listas de times do Brasileirão: {times}')
#5 primeiros colocados:
print('-=' * 30)
print(f'Os 5 primeiros colocados são: {times[:5]}')
#4 últimos colocados
print('-=' * 30)
print(f'Os 4 últimos são: {times[-4:]}')
#ordem alfabética
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
#posição da Chapecoense
print('-=' * 30)
print(f'A Chapecoense está na {times.index('Chapecoense') + 1}º posição')