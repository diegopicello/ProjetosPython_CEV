#A repetição deve ocorrer até que o usuário perca apenas!
import random
escolhapc = ''
print('-' * 30)
print('Vamos jogar par ou ímpar!')
print('-' * 30)
while True:
    escolhauser = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if escolhauser not in 'PpIi':
        print('Digite apenas "P" ou "I"!')
    else:
        if escolhauser == 'P':
            escolhapc = 'I'
        else:
            escolhapc = 'P'
        dedos = int(input('Digite um valor inteiro entre 0 e 10: '))
        if dedos not in [0, 10]:
            print('Digite um número entre 0 e 10!')
        else:
            dedospc = random.randint(0, 10)
            soma = dedos + dedospc
            print(f'Você jogou {dedos} e o PC, {dedospc}.')
            if soma % 2 == 0:
                print(f'O total deu {soma}, que é PAR!')
                if escolhauser == 'P':
                    print('Você venceu!')
                else:
                    print('Você perdeu!')
                    break
            else:
                print(f'O total deu {soma}, que é ÍMPAR!')
                if escolhauser == 'I':
                    print('Você venceu!')
                else:
                    print('Você perdeu!')
                    break
