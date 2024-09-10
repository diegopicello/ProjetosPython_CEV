'''Faça um programa que tenha uma função notas() que pode receber 
várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)
'''
def notas(* valores, sit = True):
    dados = {}
    dados['total'] = len(valores)
    somatotal = 0
    for c in range(0, len(valores)):
        somatotal += valores[c]
        if c == 0:
            maior = menor = valores[c]
        elif valores[c] < menor:
            menor = valores[c]
        if valores[c] > maior:
            maior = valores[c]
        c += 1
    media = somatotal/len(valores)
    dados['Maior'] = maior
    dados['Menor'] = menor
    dados['Média'] = media
    if sit:
        if media >=5:
            dados['Situação'] = 'Boa!'
        else:
            dados['Situação'] = 'Ruim!'
    return(dados)

#Programa principal:
resposta = notas(5.5, 2.5, 1.5, sit = False)
print(resposta)
