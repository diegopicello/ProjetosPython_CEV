resp = 'sim'
soma = cont = 0
primeiro = float(input('Digite um número: '))
soma += primeiro
menor = maior = primeiro
cont = 1
resp = str(input('Quer continuar?[s/n] ')).lower().strip()[0]
while resp not in 'Nn':
    num = float(input('Digite um número: '))
    soma += num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    cont += 1
    resp = str(input('Quer continuar?[s/n] ')).lower().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi de {}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
