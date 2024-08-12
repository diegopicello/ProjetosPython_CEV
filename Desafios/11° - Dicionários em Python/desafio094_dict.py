'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''
aluno = dict()
alunos = list()
quer = 'Ss'
while True:
    aluno['Nome'] = str(input('Nome do aluno: '))
    aluno['Média'] = float(input('Média do aluno: '))
    if aluno['Média'] < 7:
        aluno['Situação'] = 'de recuperação'
    else:
        aluno['Situação'] = 'Aprovado'
    alunos.append(aluno.copy())
    quer = str(input('Quer continuar? [S/N]'))
    if quer in 'Nn':
        break
for a in range(0, len(alunos)):
    if a < len(alunos) - 1:
        print(f'O aluno(a) {alunos[a]["Nome"]} tem média {alunos[a]["Média"]} e está de {alunos[a]["Situação"]};')
    elif a == len(alunos) - 1:
        print(f'O aluno(a) {alunos[a]["Nome"]} tem média {alunos[a]["Média"]} e está de {alunos[a]["Situação"]}.')