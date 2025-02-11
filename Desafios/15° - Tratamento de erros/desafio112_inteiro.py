'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaint(texto):
    while True:        
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
                print('ERRO! Digite um número válido.')
                continue
        except KeyboardInterrupt:
             print('Entrada de dados interrompida pelo usuário.')
             return 0
        else:
             return n  


num = leiaint('Digite um número: ')
print(f'O valor digitado foi {num}.')

