import datetime
n18mais = 0
n18menos = 0
anoAtual = datetime.datetime.now().year
for c in range(1, 8):
    anoNasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if (anoAtual - anoNasc) >= 18:
        n18mais += 1
    else:
        n18menos += 1
print('há {} maiores de idade e {} menores de idade.'.format(n18mais, n18menos))
