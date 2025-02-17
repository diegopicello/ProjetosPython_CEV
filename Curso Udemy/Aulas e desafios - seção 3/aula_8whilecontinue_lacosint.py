#Continue: pula resto do while e volta ao início do laço;

print('='*30)
print(f'{' Cadastro ':=^30}')
print('='*30)
quer = 's'
pessoas = []

while quer not in 'Nn':
    pessoa = []
    nome = input('Digite seu nome: ')
    pessoa.append(nome)
    queridade = input('Quer digitar a idade?')
    if queridade in 'Nn':
        pessoas.append(pessoa)
        continue
    idade = input('Digite a idade: ')
    pessoa.append(idade)
    pessoas.append(pessoa)
    print(pessoa)
    quer = input('Quer continuar? ')
print(pessoas)

