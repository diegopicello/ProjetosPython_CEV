'''Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(Digite um n: )'''
def leiaint(texto):
    while True:
        n = str(input(texto)).strip()
        if n.isnumeric() is False:
            print('ERRO! Digite um número válido.')
        else:
            return n

#programa principal:
n = leiaint('Digite um número: ')
print(f'Você digitou o valor {n}')
