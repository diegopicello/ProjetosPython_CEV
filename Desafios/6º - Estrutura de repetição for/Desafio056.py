totanos = 0
maisvelho = 0
tot20 = 0
nomemaisvelho = str('')
tothomem = 0
totmulher= 0
for p in range (1, 5):
    print(6 * '=-', "{}º pessoa".format(p), 6 * '=-')
    nome = str(input("Primeiro nome: ")).strip().title()
    idade = int(input('Idade: '))
    totanos += idade
    sexo = str(input('Sexo [M/F]: ')).strip().capitalize()
    if sexo == 'M':
        tothomem += 1
        if idade > maisvelho:
            maisvelho = idade
            nomemaisvelho = nome
    else:
        if idade < 20:
            tot20 += 1
media = totanos / 4
print('A média de idade do grupo é de {} anos.'.format(media))
if tothomem == 0:
    print('não há homens.')
elif tothomem == 1:
    print('Há apenas um homem, o qual tem {} anos e se chama {}.'.format(maisvelho, nomemaisvelho))
else:
    print('O homem mais velho tem {} anos e se chama {}.'.format(maisvelho, nomemaisvelho))
if tot20 > 1:
    print('Ao todo, são {} mulheres com menos de 20 anos.'.format(tot20))
elif tot20 == 1:
    print('Há apenas uma mulher com menos de 20 anos.')
else:
    print('Não há mulheres com menos de 20 anos.')
    