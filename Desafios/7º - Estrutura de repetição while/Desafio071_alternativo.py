cedula, totcedula = 50, 0
print('=' * 30)
print('{:^30}'.format("Didico's Bank"))
print('=' * 30)
valor = int(input('Quanto você deseja sacar? '))
total = valor
while True:
    total -= cedula
    totcedula += 1
    if total < cedula:
        if totcedula > 0:
            print(f'{totcedula} cédulas de {cedula}.')
        totcedula = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
    if total == 0:
        break
