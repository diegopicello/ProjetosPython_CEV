valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for cont, valor in enumerate(valores):
    print(f'na posição {cont}, encontrei o valor {valor}...', end = '')
print('Cheguei ao fim da lista.')