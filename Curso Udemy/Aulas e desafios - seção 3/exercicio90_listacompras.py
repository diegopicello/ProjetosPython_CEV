import os
listacompras = ['Feijão','Arroz','Leite']

while True:
    for i, produto in enumerate(listacompras):
        print(i, produto)
    print('Selecione uma opção: ')
    escolha = input('[i]nserir [a]pagar [l]istar [s]air: ').strip()
    if escolha in 'Ll':
        if len(listacompras) == 0:
            print('Nada para listar.')
        else:
            for indice, produto in enumerate(listacompras):
                print(indice, produto)
    elif escolha in 'Ss':
        break
    elif escolha in 'Aa':
        try:
            ind_apagar = int(input('Digite o índice que deseja apagar: '))
            del listacompras[ind_apagar]
        except IndexError:
            print('Erro: índice digitado não existe na lista.')
        except ValueError:
            print('Erro: digite apenas números inteiros.')
    elif escolha in 'Ii':
        os.system('clear')
        novoitem = input('Digite o produto a ser inserido: ')
        listacompras.append(novoitem)
    else:
        print('Por favor, digite apenas valores válidos.')
