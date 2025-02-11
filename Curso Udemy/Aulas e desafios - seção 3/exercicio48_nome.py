nome = str(input('Digite seu nome: '))
idade = str(input('Digite sua idade: '))
if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    if ' ' in nome:
        print('Seu nome possui espaços.')
    else:
        print('Seu nome não contém espaços.')
    print(f'A primeira letra do seu nome é {nome[0].lower()}.')
    print(f'A última letra do seu nome é {nome[-1].lower()}')
else:
    print('erro: há campos vazios.')
