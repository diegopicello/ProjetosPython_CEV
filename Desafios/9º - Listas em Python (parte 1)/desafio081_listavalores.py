lista = []
continuar = "s"
maior == menor == 0
tem5 = False
while "Nn" not in continuar:
    valor = int(input("Digite um número: "))
    while tem5 == False:
        if valor != 5:
            tem5 = False
        else:
            tem5 = True
    lista.append(valor)
    continuar = str(input("Quer continuar? [S/N]")).lower().strip()
print(f"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são: {lista.sort(reverse = True)}")
if tem5 == True:
    print("O cinco faz parte da lista!")
else:
    print("O cinco não faz parte da lista!")
    