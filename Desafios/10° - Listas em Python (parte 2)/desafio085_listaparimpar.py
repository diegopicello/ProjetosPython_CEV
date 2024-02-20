'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''
pares = []
impares = []
todos = []
for c in range (1,8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
pares.sort()
impares.sort()
todos.append(pares)
todos.append(impares)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitadosforam: {impares}')
print(f'A lista total é: {todos}') #OBS: poderia ter declarado a lista maior diretamente no início.
