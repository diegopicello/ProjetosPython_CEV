nome = str(input('Qual é seu nome? ')).strip().capitalize()
if nome == 'Diego':
    print('Que nome lindo você tem!')
else:
    print('Que nome sem graça!')
print('Bom dia, {}!'.format(nome))
