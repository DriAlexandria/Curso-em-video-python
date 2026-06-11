frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))
#Resultado = 3
#count para contar o que vc quiser em específico
#Upper para que o resultado considere tudo maiúsculo (independente do que for digitado)

print(len(frase))
##len para contar as letras da frase
print(len(frase.strip()))
#strip para contar as letras sem contar os espacos antes e depois

print(frase.replace('Python', 'Android'))
#ou...
frase = frase.replace('Python', 'Ándroid')
print(frase)
#replace para substituir uma palavra por outra por exemplo "trocar antigo por novo": .replce('Antigo', 'Novo')

frase = 'Curso em Vídeo Python'
print('Curso' in frase)
#True

print(frase.find('Vídeo'))
#True (pq tem V)

print(frase.find('vídeo'))
#false (pq tem v)
#find para saber a posição em que a palavra que quer está

print(frase.lower().find('video'))
#9
#lower para transformar tudo em minúsculo

print(frase.split())
#['Curso', 'em', 'Vídeo', 'Python']

dividido = frase.split()
print(dividido[0])
#Curso
#split para dividir uma frase em uma lista de pedaços menores.

junto = ''.join(frase)
#CURSOEMVIDEOPYTHON
#''.join para juntar tudo depois do split, se vc quiser que tenha algo entre as palavras, deve botar esse "algo" dentro das aspas simples ex: '-'.

print("""Ajenub;qwjnJddjcn;in:KajnfOfpf.
      JAw;foaiuchlKnrfr;lishhcóknkjenfrídf
      jefh;oiuchlknfkmn;kjdhndíwNEF'LKNC
      JBFWOwulJKNSdlcn;oesb;'LKSJníp""")
