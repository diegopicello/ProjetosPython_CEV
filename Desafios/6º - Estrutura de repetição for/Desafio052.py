from colorama import init
n = int(input('Digite um número: '))
nDiv = 0
for c in range (1, n + 1):
    init()
    if n % c == 0:
        nDiv += 1
        print('\033[;0;36;40m{} \033[m'.format(c), end = '')
    else:
        print('\033[;0;31;40m{} \033[m'.format(c), end = '')
print('')
print('o número {} foi dvisível em {} ocasiões '.format(n, nDiv), end = '')
if nDiv != 2:
    print('e, por isso, não é primo.')
else:
    print('e, por isso, é primo.')

    


