s = ''
s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while s not in ('M', 'F'):
    print('Opção inválida!')
    s = str(input('Tente informar novamente [M/F]: '))
print('Fim.')
