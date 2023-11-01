'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
listaimpar = []
listapar = []
quer = 's'
while True:
    valor = int(input('Digite um número: '))
    lista.append(valor)
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    quer = str(input('Quer continuar[S/N]: ')).strip()
    if quer in 'Nn':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de números pares é: {listapar}')
print(f'A lista de números ímpares é: {listaimpar}')
