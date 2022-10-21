#peculiaridade do python nas listas:
a = [2, 3, 4, 7]
#b = a
#a partir do momento que você faz uma lista receber outra, python cria ligação entre elas: o que faz em uma, faz na outra!
#python não cria cópia através do operador "recebe"!
b = a[:]#fatiamento (faz receber todos os itens de A): esse formato faz b receber cópia dos valores, e não uma ligação!
b[2] = 8
print(f'lista a: {a}')
print(f'lista b: {b}')