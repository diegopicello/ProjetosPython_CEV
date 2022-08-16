from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
print('Você tem {} anos em {}.'.format(idade, atual))
if idade < 18:
    print('Ainda faltam {} anos para seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
elif idade == 18:
    print('Você deve se alistar imediatamente!')
else:
    print('Seu alistamento foi há {} anos, em {}.'.format(idade - 18, atual - (idade - 18)))
    print('Apresente-se à Junta Militar mais próxima e quite seu débito.')
    