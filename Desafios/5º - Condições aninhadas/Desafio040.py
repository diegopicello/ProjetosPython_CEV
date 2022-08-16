p1 = float(input('Insira a primeira nota: '))
p2 = float(input('Insira a segunda nota: '))
m = (p1 + p2) / 2
print('Sua média foi de {}.'.format(m))
if m >= 7:
    print('Você foi aprovado!')
elif m >= 5 and m < 7:
    print('Você está de recuperação.')
else:
    print('Você foi REPROVADO!')
