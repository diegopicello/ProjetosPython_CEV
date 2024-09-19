'''Funções para cálculos básicos, como aumento, dobro, etc.'''
def aumentar(valor, tanto):
    '''---> Calcula o aumento do valor;
    parâmetro valor: o input que será aumentado;
    parâmetro tanto: a magnitude do aumento;
    retorno: o valor aumentado em (1 + tanto)%.'''
    valor *= (1 + tanto)
    return valor

def diminuir(valor, tanto):
    '''---> Calcula a diminução do valor;
    parâmetro valor: o input que será diminuído;
    parâmetro tanto: a magnitude da diminuição;
    retorno: o valor diminuído em tanto% dele.'''
    valor *= tanto
    return valor

def dobro(valor):
    '''---> Calcula a metade do parâmetro valor.'''
    valor *= 2
    return valor

def metade(valor):
    '''---> Calcula a metade do  parâmetro valor.'''
    valor *= 0.5
    return valor

def moeda(valor):
    return f'R${valor:.2f}'.replace('.',',')
print(moeda(200))
