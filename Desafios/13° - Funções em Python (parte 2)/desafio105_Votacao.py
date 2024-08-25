'''Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(year):
    from datetime import date
    atual = date.today().year
    idade = atual - year
    print(f'Com {idade} anos ', end='')
    if idade < 16:
        return'não vota.'
    elif 18 <= idade <= 65:
        return'o voto é obrigatório.'
    else:
        return'o voto é opcional.'


ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
