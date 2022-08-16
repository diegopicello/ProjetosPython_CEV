for c in range (1, 51):
    if c % 2 == 0:
        print(c, end = ' ')
print('finish')

#ou
#for c in range (2, 51, 2):
#    print(c, end = ' ')
#print('finish')
#essa economiza a memória, pois o que influencia mais não é o número de linhas, mas o número de repeticões: No primeiro caso, ele repete 50 vezes
#pois dá passo 1 mesmo que só queira os pares. no segundo, ele só faz 25 repetiçõess(só conta esses 25), pois vai de 2 em 2 já! No outro, ele faz
#o "movimento" de contar 50 vezes mas só pega 25 números, gastando memória e processador sem necessidade!


