frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))
#3
#count para contar o que vc quiser em específico

print(len(frase))
##len para contar as letras da frase
print(len(frase.strip()))
#strip para contar as letras sem contar ops espacos antes e depois

print(frase.replace('Python', 'Android'))
#ou...
frase = frase.replace('Python', 'Ándroid')
print(frase)

frase = 'Curso em Vídeo Python'
print('Curso' in frase)
#True

print(frase.find('Vídeo'))
#True (pq tem V)

print(frase.find('vídeo'))
#false (pq tem v)

print(frase.lower().find('video'))
#9

print(frase.split())
#['Curso', 'em', 'Vídeo', 'Python']

dividido = frase.split()
print(dividido[0])
#Curso

print("""Ajenub;qwjnJddjcn;in:KajnfOfpf.
      JAw;foaiuchlKnrfr;lishhcóknkjenfrídf
      jefh;oiuchlknfkmn;kjdhndíwNEF'LKNC
      JBFWOwulJKNSdlcn;oesb;'LKSJníp""")
