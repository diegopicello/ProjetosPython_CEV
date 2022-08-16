sal = float(input('Qual é o seu salário atual? '))
if sal <= 1250:
    novoSal = sal * 1.15
else:
    novoSal = sal * 1.1
print('Seu novo salário é de R${:.2f}. '.format(novoSal))
