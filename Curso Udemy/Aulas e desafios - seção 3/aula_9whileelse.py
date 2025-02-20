"""else é executado quando o while é executado por completo
se saio por um break, o else não é executado: saída forçada"""

i = 0
nome = input('Digite um nome: ')
while i < len(nome):
    letra = nome[i]
    print(letra)
    if letra == ' ':
        print(f'Encontrei espaço no índice {i}.')
        break
    i += 1
else:
    print('Não há espaços nesse nome.')
