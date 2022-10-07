quer = sexo = ' '
totmaior = tothomem = totmulher20 = idade = 0
while quer not in 'Nn':
    print('=' * 20)
    print('Cadastre uma pessoa')
    print('=' * 20)
    while idade <= 0:
        idade = int(input('Idade: '))
    if idade > 18:
        totmaior += 1
    while sexo not in 'MmFf':
        sexo = str(input('sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        tothomem += 1
    else:
        if idade < 20:
            totmulher20 += 1
    while quer not in 'SsNn':
        quer = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print(f'Total de pessoas com 18 anos ou mais: {totmaior}')
if tothomem == 1:
    print('Ao todo, 1 homem foi cadastrado.')
elif tothomem == 0:
    print('Nenhum homem foi cadastrado.')
else:
    print(f'Ao todo, {tothomem} homens foram cadastrados.')
if totmulher20 == 1:
    print('Ao todo, 1 mulher com menos de 20 anos foi cadastrada.')
elif totmulher20 == 0:
    print('Nenhuma mulher com menos de 20 anos foi cadastrada.')
else:
    print(f'{totmulher20} mulheres com menos de 20 anos foram cadastradas')
