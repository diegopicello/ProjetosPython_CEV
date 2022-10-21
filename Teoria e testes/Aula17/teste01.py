num = [2, 5, 9, 1]
num[2] = 3
#num[4] = 7 #não posso adicionar valor assim! dará erro
num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
num.pop(2) #perceba que o pop só remove o primeiro elemento, a primeira ocorrencia do valor que você quer eliminar.
#além disso, o pop dá erro se tenta remover algo que não está na lista!
print(num)
print(f'Essa lista tem {len(num)} elementos.')
