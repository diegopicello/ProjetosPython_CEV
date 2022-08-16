peso = float(input('Digite sua massa em Kg: '))
altura = float(input('Digite sua altura em m: '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!.')
elif imc >= 18.5 and imc < 25:
    print('Parabéns! Você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Cuidado! Obesidade atingida!')
elif imc > 40:
    print('busque um médico imediatamente: obesidade mórbida!')
