'''Funções para cálculos básicos, como aumento, dobro, etc.'''
def moeda(valor, cifrão = 'R$'):
    '''---> formata um valor float qualquer para um valor monetário;
    parâmetro valor: o valor a ser formatado;
    parâmetro cifrão: a moeda nacional a ser utilizada;
    retorno: o valor formatado.'''
    return f'{cifrão}{valor:.2f}'.replace('.',',')

def aumentar(valor, tanto, formatação = True):
    '''---> Calcula o aumento do valor;
    parâmetro valor: o input que será aumentado;
    parâmetro tanto: a magnitude do aumento;
    retorno: o valor aumentado em (1 + tanto)%.'''
    valor *= (1 + tanto)
    if formatação:
        novovalor = moeda(valor)
    return novovalor

def diminuir(valor=0 , tanto = 0, formatação = True):
    '''---> Calcula a diminução do valor;
    parâmetro valor: o input que será diminuído;
    parâmetro tanto: a magnitude da diminuição;
    retorno: o valor diminuído em tanto% dele.'''
    valor *= tanto
    if formatação:
        novovalor = moeda(valor)
    return novovalor

def dobro(valor, formatação = True):
    '''---> Calcula a metade do parâmetro valor;
    parâmetro valor: o valor utilizado para o cálculo;
    parâmetro formatação: apresentar valor com formatação monetária;
    retorno: o dobro do valor com formatação monetária.'''
    valor *= 2
    if formatação:
        novovalor = moeda(valor)
    return novovalor

def metade(valor, formatação = True):
    '''---> Calcula a metade do  parâmetro valor;
    parâmetro valor: o valor utilizado para o cálculo;
    parâmetro formatação: apresentar valor com formatação monetária;
    retorno: a metade do valor com formatação monetária.'''
    valor *= 0.5
    if formatação:
        novovalor = moeda(valor)
    return novovalor

def resumo(valor, aumento, diminuição):
    '''--->Resume as funções anteriores em uma única:
    parâmetro valor: a base de cálculo;
    parâmetro aumento: taxa do aumento;
    parâmetro diminuição: taxa do desconto.'''
    print('='*23)
    print('  Resumo dos valores:')
    print('='*23)
    print(f'Preço analisado: {moeda(valor)};')
    print(f'Dobro do preço: {dobro(valor)};')
    print(f'Metade do valor: {metade(valor)};')
    print(f'Valor reduzido em {diminuição}%: {diminuir(valor, (100-diminuição)/100)};')
    print(f'Valor aumentado em {aumento}%: {aumentar(valor, aumento/100)};')
