n = 1
print('=-' * 10)
print('Gerador de PA')
print('=-' * 10)
a1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
an = a1
for c in range(10, -1, -1):
    if c == 0:
        print('PAUSA')
    else:
        print('{} -> '.format(an), end = '')
        an = an + r     
while n != 0:
    n = int(input('Quantos termos subsequentes você ainda quer mostrar? '))
    if n == 0:
        print('Fim da execução.')
    else:
        for c in range(n, -1, -1):
            if c != 0:
                print('{} -> '.format(an), end = '')
                an = an + r
            else:
                print('PAUSA')