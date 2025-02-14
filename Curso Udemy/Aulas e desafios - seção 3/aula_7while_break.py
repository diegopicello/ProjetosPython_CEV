#while: executa ação enquanto uma condição for verdadeira;
#cuidado com loops infinitos;
#Para parar: tornar a condição em falsy ou colocar um break;
#o break procura o laço mais próximo;
nomes = []
while True:
    nome = input('digite um nome: ')
    if nome == 'sair':
        break
    nomes.append(nome)
print(f'Os nomes digitados foram: {nomes}')

CONTADOR = 0
while CONTADOR < 10:
    CONTADOR += 1
    print(CONTADOR,end=' ')

print('Contei até 10.')
