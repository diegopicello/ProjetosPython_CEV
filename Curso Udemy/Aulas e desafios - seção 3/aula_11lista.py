#lista é tipo mutável;
#iterável e fatiável;
#append, insert, pop, del, clear, extend...
lista = []
print(bool(lista))#lista vazia é um falsy
cidades = ['Barra Bonita', 'Ribeirão Preto', 'Jaú', 'Bauru']
cidades[1] = 'Rio Preto'
print(cidades[-1], type(cidades[1]))
print(cidades[1])
cidade = cidades[1]
print(cidade)
del cidades[0] #é mais interessante trabalhar com final da lista via pop e append: tirar um item e realocar o resto exigem processamento demais
cidades.append('Mirassol')
cidades.append('Andradina')
cidades.append('Campinas')
cidades.append('Pereira Barreto')
ultima_deletada = cidades.pop() #o pop retorna o que deletou;
print(cidades,f'Última deletada: {ultima_deletada}')
tirei = cidades.pop(3)
print(cidades, f'tirei a cidade de {tirei}')#posso usar pop para tirar do meio ou começo, mas evitar em lista grande;
