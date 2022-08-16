#1º etapa: estruturar a frase inicial, deixando-a sem espaços e toda maiúscula.
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.split()
frase = ''.join(frase)

#2º etapa: com a frase estruturada, precisamos criar uma lista com cada letra sendo indexada e uma variável com a length da lista.
listaLet = frase[:]
compri = len(listaLet)

#3º etapa: formar a frase espelho e analisar um possível palíndromo.
novaFrase = ''
for c in range (1, (compri + 1)):
    novaFrase += listaLet[(compri - c)]
print('"{}" ao contrário e sem contar espaços é "{}", '.format(frase, novaFrase), end = '')
if frase == novaFrase:
    print('portanto, é um palíndromo.')
else:
    print('portanto, não é um palíndromo.')







