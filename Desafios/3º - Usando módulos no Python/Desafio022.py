nome = input('Digite seu nome completo: ')
nomeformat = nome.strip()
totEspaço = nomeformat.count(' ')
totLetras = len(nomeformat) - totEspaço
nomediv = nomeformat.split()
tLP = len(nomediv[0])    #tLP significa total Letras Primeiro elemento de split
print('ANALISANDO SEU NOME...')
print('Seu nome em maiúsculas é {}.'.format(nomeformat.upper()))
print('Seu nome em minúsculas é {}.'.format(nomeformat.lower()))
print('Seu nome tem, ao todo, {} letras.'.format(totLetras))
print('Seu primeiro nome é {} e tem o total de {} letras.'.format(nomediv[0], tLP))
#print('Seu primeiro nome é {} e tem o total de {} letras.'.format(nomediv[0], nome.find(' '))) : assim daria certo também

