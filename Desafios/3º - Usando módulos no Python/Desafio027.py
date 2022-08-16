nome = str(input('Digite seu nome completo: ')).title().strip()
listaNome = nome.split()
ultimoNome = listaNome[::-1]
print('Muito prazer, {}!'.format(nome))
print('Seu primeiro nome é {}.'.format(listaNome[0]))
print('Seu último nome é {}.'.format(ultimoNome[0]))

#Caminho Alternativo:
#print('Seu último nome é {}.'.format(listaNome[len(nome) - 1]))
#perceba que len mostra a quantidade de itens na lista, mas os índices começam em zero;
#logo, é necessário colocar "-1" para retirar o número excedente que vem da função len()!