n = int(input('Digite um número inteiro não negativo para calcular seu fatorial: '))
c = n
f = 1 #tem que começar com 1 pois o 1 é o fator nulo de multiplicação e divisão. Só usa 0 em soma e subtração. É o um que mantém uma multiplicação limpa!
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)