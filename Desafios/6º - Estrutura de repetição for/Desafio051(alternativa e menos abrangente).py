print(11 * '=-')
print(' 10 TERMOS DE UMA P.A')
print(11 * '=-')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = t + 9 * r
for c in range(t, décimo + r, r):
    print(c,' -> ', end = '')
print('Fim.')

#perceba que este, por usar t e r no range da repetição, tais variáveis não podem ser float, tendo em vista que não existe
#1,5 vezes em uma repetição de uma instrução, por exemplo! (não existe meia repetição num programa)
