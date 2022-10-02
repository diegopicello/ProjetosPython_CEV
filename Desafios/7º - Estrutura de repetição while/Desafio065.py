soma = cont = 0
primeiro = float(input('Digite um número: '))
soma += primeiro
menor = maior = primeiro
cont = 1
sn = str(input('Quer continuar?[s/n] '))
while 'n' not in sn:
    num = float(input('Digite um número: '))
    soma += num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    cont += 1
    sn = str(input('Quer continuar?[s/n] '))
media = soma / cont
print('Você digitou {} números e a média foi de {}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
