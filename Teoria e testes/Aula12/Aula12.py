nome = str(input('Qual é seu nome? '))
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular no Brasil.')
elif nome in ('Ana Cláudia Jéssica Juliana'):
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}.'.format(nome))


