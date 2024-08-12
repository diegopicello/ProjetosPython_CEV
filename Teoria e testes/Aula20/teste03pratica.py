def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(s)

def dobra(lista):
    pos = 0
    print(lista)
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(lista)

soma(3, 2, 7)
soma(1, 1, 1, 1, 1, 1)
dobra([1, 2, 4, 8])
