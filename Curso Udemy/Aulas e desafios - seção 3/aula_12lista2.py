"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas (polimorfismo)
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)"""
#o pop também retorna um valor
lista1 = [1,2,3,4]
lista2 = ['Diego','Laura',3,7]
lista1.append('Laura')
nome = lista1.pop()
print(nome)
print(lista1)
lista1.append(12456)
print(lista1)
del lista1[-1]
print(lista1)
#se não passa índice, pop tira o último, mas pode dizer um índice;
#insert só serve escolhendo índice
lista1.insert(0,'Diego')
print(lista1)
lista1.insert(50000000,'Alan')
#número muito grande maior que a lista: joga no último;
lista1.extend(lista2)
#extende faz ação mas não entrega valor, logo, se faz extend na lista a, muda a lista a
print(lista1)
