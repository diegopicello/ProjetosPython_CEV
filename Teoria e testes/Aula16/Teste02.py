lanche = ('Hambúrger', 'suco', 'pizza', 'pudim')
print(lanche)
print(sorted(lanche))#sorted = organizado em ordem: a tupla não foi mudade: entenderemos o que ocorreu na aula de listas!
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)#a ordem aqui importa: a + b fica 2, 5, 4, 5, 8, 1, 2, já b + a ficaria 5,8,1,2,2,5,4
print(c.count(5)) #conta quantas vezes 5 aparece na tupla c
print(c.index(8)) #mostra a posição do número que pdimos dentro da tupla. Esse método sempre pega a primeira ocorrência EX: na tupla C, só mostraria a primeira ocorrencia de 2
print(c.index(5, 2))
