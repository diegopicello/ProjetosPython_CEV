n = 0
s = 0
for c in range (1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            n += 1
            s += c
print('A soma dos {} valores solicitados é {}.'.format(n, s))

