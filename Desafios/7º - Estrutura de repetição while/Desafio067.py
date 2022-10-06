num = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    if num == 0:
        print('Qualquer número multiplicado por zero dá zero!')
    else:
        for c in range(1, 11):
            print(f'{num} x {c} = {(num * c)}')
            c += 1
print('Fim da execução. Obrigado!')
    