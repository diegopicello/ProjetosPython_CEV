def leiaDinheiro(texto):
    '''---> Valida dados monetários: só para ao encontrar um dado, de fato, numérico;
    parâmetro texto: o texto que aparecerá antes do usuário inserir os dados;
    retorna: o valor numérico validado.
    '''
    while True:
        valor = str(input(texto)).strip().replace(',','.')
        if valor.replace('.','').isnumeric() is False:
            print(f'ERRO! {valor} não é um valor válido.')
        else:
            break
    return float(valor)
    