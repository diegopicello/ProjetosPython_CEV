valor = float(input('Qual é o valor do imóvel desejado? '))
sal = float(input('Qual é seu salário atual? '))
tempoMeses = 12 * int(input('Em quantos anos você deseja financiar? '))
parcela = valor/tempoMeses
print('Para financiar uma casa de {} em {} anos, a parcela será de {:.2f}.'.format(valor, tempoMeses/12, parcela))
if parcela > (0.3*sal):
    print('Seu financiamento foi negado.')
else:
    print('Seu financiamento foi aprovado.')
