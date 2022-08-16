vatual = float(input('Qual é a velocidade atual do carro? '))
vlimite = 80
if vatual <= vlimite:
    print('Tenha um bom dia. Dirija com cuidado!')
else:
    valormulta = (vatual - vlimite) * 7
    print('Multado! você excedeu a velocidade permitida de 80km/h')
    print('Você deve pagar uma multa de {:.2f}R$'.format(valormulta))

