c = 0
print('=-' * 10)
print('Gerador de PA')
print('=-' * 10)
a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite o valor da razão da PA. '))
an = a1
while c <= 10:
    if c != 10:
        print('{} -> '.format(an), end = '')
    else:
        print('FIM')
    an = an + r
    c += 1
