'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
dados = dict()
dados['Nome'] = str(input('Digite o nome: '))
dados['ano nasc'] = int(input('Digite o ano de nascimento: '))
idade = 2024 - dados['ano nasc']
dados['Nº carteira'] = int(input('Digite o número da Carteira de Trabalho (digite "0" caso não tenha): '))
if dados['Nº carteira'] != 0:
    dados['Ano de contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o valor nominal do salário: '))
    dados['idadetrab'] = dados['Ano de contratação'] - dados['ano nasc']
    dados['idadeaposent'] = dados['idadetrab'] + 30
    for i, v in dados.items():
        print(f'{i} tem valor {v}.')
