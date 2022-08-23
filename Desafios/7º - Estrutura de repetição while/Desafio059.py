from time import sleep
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
sair = False
while sair == False:    
    print('[1] somar;')
    print('[2] multiplicar;')
    print('[3] maior;')
    print('[4] novos números;')
    print('[5] sair do programa.')
    escolha = int(input('Qual é a sua opção? '))
    if escolha not in list(range(1,6)):
        print('Opção inválida! Tente novamente.')
    elif escolha == 5:
        sair = True
    else:
        if escolha == 1:
            print('A soma entre {} e {} é igual a {}.'.format(v1, v2, (v1 + v2)))
            sleep(2)
        elif escolha == 2:
            print('{} x {} = {}'.format(v1, v2, (v1 * v2)))
            sleep(2)
        elif escolha == 3:
            maior = 0
            if v1 != v2:
                if v1 > v2:
                    maior = v1
                elif v1 < v2:
                    maior = v2
                print('O maior entre os 2 valores digitados é {}.'.format(maior))
            else:
                print('Ambos os valores são iguais.')
            sleep(2)        
        else:
            v1 = float(input('Primeiro valor: '))
            v2 = float(input('Segundo valor: '))
            sleep(2)    
print('Fim da execução.')
