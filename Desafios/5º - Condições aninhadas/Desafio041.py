from datetime import date
nasc = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você se enquadra na categoria Mirim.')
elif idade > 9 and idade <= 14:
    print('Você se enquadra na categoria Infantil.')
elif idade > 14 and idade <= 19:
    print('Você se enquadra na categoria Júnior.')
elif idade > 19 and idade <= 25:
    print('Você se enquadra na categoria Sênior.')
else:
    print('Você se enquadra na categoria Master.')
