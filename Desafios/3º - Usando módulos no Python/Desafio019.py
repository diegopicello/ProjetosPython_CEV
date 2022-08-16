from random import choice
a1 = str(input('primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
sort = choice(lista)
print('O aluno sorteado foi {}.'.format(sort))

