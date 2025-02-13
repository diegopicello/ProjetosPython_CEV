"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')

comprimentonome = len(nome)
nomecurto = comprimentonome <= 4
nomenormal = 5 <= comprimentonome <= 6
nomelongo = comprimentonome > 6

if nomecurto:
    print(f'{nome} é um nome curto.')
if nomenormal:
    print(f'{nome} é um nome normal.')
if nomelongo:
    print(f'{nome} é um nome longo.')
