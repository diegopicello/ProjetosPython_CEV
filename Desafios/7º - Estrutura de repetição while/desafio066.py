totnum = soma = 0

while True:
    num = float(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    soma += num
    totnum += 1
print(f'A soma dos {totnum} valores digitados foi de {soma}.')