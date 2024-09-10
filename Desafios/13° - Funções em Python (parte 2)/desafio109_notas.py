'''Faça um programa que tenha uma função notas() que pode receber 
várias notas de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)
'''
def notas(* valores, sit = True):
    '''-> Cria um dicionário contendo:
    * o total de valores digitados;
    * o maior valor da lista de notas;
    * o menor valor da lista de notas;
    * a média da lista de notas;
    * a situação da turma, sendo um parâmetro opcional.
    '''
    dados = {}
    dados['total'] = len(valores)
    '''somatotal = 0
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
    dados['Média'] = media'''
    dados['Maior'] = max(valores)
    dados['Menor'] = min(valores)
    dados['Média'] = sum(valores)/len(valores)
    if sit:
        if dados['Média'] >=5:
            dados['Situação'] = 'Boa!'
        else:
            dados['Situação'] = 'Ruim!'
    return dados

#Programa principal:
resposta = notas(5.5, 2.5, 1.5, sit = False)
print(resposta)
help(notas)
