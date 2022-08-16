palavras = str(input('Digite uma frase: ')).strip().lower()
quantA = palavras.count('a')
print('A letra "A" aparece {} vezes na frase.'.format(quantA))
primeiraA = palavras.find('a')
print('A primeira letra "A" aparece na posição {}.'.format(primeiraA + 1))
palavrasInvert = palavras[::-1]
ultimaAnormal = len(palavrasInvert) - palavrasInvert.find('a')
print('A última letra "A" aparece na posição {}.'.format(ultimaAnormal))

#Forma alternativa de fazer a contagem da última letra:
#print('A última letra "A" aparece na posição {}.'.format(palavras.rfind('a') + 1)
#perceba que esse método não inverte a string, mas sim acha a posição da última "A" considerando
#os índices da string padrão (ex: o rfind vai achar o último "A" na posição 30 da string padrão)