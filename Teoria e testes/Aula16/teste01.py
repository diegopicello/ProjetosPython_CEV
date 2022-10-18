lanche = ('Hambúrger', 'suco', 'pizza', 'pudim')
'''TUPLAS SÃO IMUTÁVEIS!
lanche[1] = 'refri'''
print(lanche)
print(lanche[1])
print(lanche[-2:]) #começa no penúltimo e vai até o fim
print(lanche[1:3]) #cuidado com o último termo omitido!
for comida in lanche:
    print(comida, end = ' ')
for cont in range(0, len(lanche)):
    print(lanche[cont], end = ' ')
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}.')