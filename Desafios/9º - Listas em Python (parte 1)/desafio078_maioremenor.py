'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
valores = []
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] >= maior:
            maior = valores[c]
        if valores[c] <= menor:
            menor = valores[c]
print(30 * '=-')
print('Você digitou os valores: ', end = '')
for valor in valores:
    print(f'{valor} ', end = '')
print(f'\nO maior valor digitado foi {maior} nas posições: ', end = '')
for indice, valor in enumerate(valores):
    if valores [indice] == maior:
        print(indice, end = ' ')
print(f'\nO menor valor digitado foi {menor} nas posições: ', end = '')
for indice, valor in enumerate(valores):
    if valores[indice] == menor:
        print(indice, end = ' ')
