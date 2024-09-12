'''Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra FIM, 
o programa se encerrará. Importante: use cores.
'''
from time import sleep
def ajuda(texto):
    print('='*(30 + len(texto)))
    print(f' Acessando manual do comando {texto}')
    print('='*(30 + len(texto)))
    for c in range(0,3):
        print('. ', end='', flush=True)
        c += 1
        sleep(0.5)
    print(help(texto))


#programa principal:
func = ''
print('~'*25)
print(' Sistema de ajuda PYhelp')
print('~'*25)
while True:
    func = str(input('Digite a função ou biblioteca desejada: ')).strip()
    if func == 'FIM':
        print('='*12)
        print(' Até logo!')
        print('='*12)
        break
    ajuda(func)
