sal = float(input('Qual é o salário do funcionário? R$'))
nsal = sal * 1.15
print('Um funcionário que ganhava R${:.2f} passa a receber, com 15% de aumento, R${:.2f}.'.format(sal, nsal))