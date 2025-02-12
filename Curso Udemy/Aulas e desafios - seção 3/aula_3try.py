#para erros que não sejam de sintaxe!
idade_str = input(
    'Digite sua idade e o dobro será calculado: '
    )
try:
    idade_float = float(idade_str)
    print('Idade STR: ',idade_str)
    print('Idade FLOAT: ',idade_float)
    print(f'O dobro de {idade_str} é {idade_float*2}.')
except:
    print('Erro: digite um número válido!')
