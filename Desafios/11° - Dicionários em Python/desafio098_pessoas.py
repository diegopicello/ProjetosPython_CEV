'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. 
No final, mostre: A) Quantas pessoas foram cadastradas;
B) A média de idade;
C) Uma lista com as mulheres; 
D) Uma lista de pessoas com idade acima da média.'''
pessoa = {}
pessoas = []
quer = 'S'
total = 0
totalidade = 0
mulheres = []
while True:
    total += 1
    pessoa['Nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo[M/F]: ')).strip()
        if pessoa['sexo'] in 'MmFf':
            break
        print('Erro! Por favor, digite apenas caracteres válidos.')
    pessoa['idade'] = int(input('Digite a idade: '))
    totalidade += pessoa['idade']
    pessoas.append(pessoa.copy())
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa.copy())
    while True:
        quer = str(input('Quer continuar? [S/N]')).strip()
        if quer in 'SsNn':
            break
        print('Erro! Por favor, digite apenas caracteres válidos.')
    if quer in 'Nn':
        break
media = totalidade/total
print(f'A) Ao todo, foram cadastradas {total} pessoas;')
print(f'B) A média de idade foi de {media};')
print('C) As mulheres cadastradas foram: ',end='')
for c in range(0, len(mulheres)):
    if c < len(mulheres) - 1:
        print(f'{mulheres[c]["Nome"]}, ',end='')
    else:
        print(f'e {mulheres[c]["Nome"]}.')
print('D) As pessoas com idades acima da média são: ')
for c in range(0, len(pessoas)):
    if pessoas[c]["idade"] > media:
        print(f'{pessoas[c]["Nome"]}; ',end='')
       