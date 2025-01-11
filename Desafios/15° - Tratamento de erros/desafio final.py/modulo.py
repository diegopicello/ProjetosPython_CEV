def cabeçalho(texto):
    print(21*'=-')
    print(texto.center(42))
    print(21*'=-')

def opções(op1, op2, op3):
    print(f'Opção 1 - {op1}')
    print(f'Opção 2 - {op2}')
    print(f'Opção 3 - {op3}')

opções('Cadastrar', 'Mostrar lista', 'Sair')