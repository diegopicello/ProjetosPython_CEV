'''Iterar nova string com while'''
nome = input('Digite um nome: ')
tamanho_nome = len(nome)
contador = 0
novo_nome = ''

while contador < tamanho_nome:
    #print(f'*{nome[contador]}',end='')
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1
#print('\nNova string realizada!')
print(novo_nome)
