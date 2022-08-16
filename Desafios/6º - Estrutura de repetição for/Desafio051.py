print(11 * '=-')
print(' 10 TERMOS DE UMA P.A')
print(11 * '=-')
t = float(input('Primeiro termo: '))
r = (float(input('Razão: ')))
for c in range (1,11):
    print(t,' -> ', end = '')
    t += r
print('Fim dos 10 primeiros termos')



