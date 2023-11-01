'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista de valores, ordenada de forma decrescente; 
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
continuar = "s"
tem5 = False
while continuar not in "Nn":
    valor = int(input("Digite um número: "))
    lista.append(valor)
    continuar = str(input("Quer continuar? [S/N]")).lower().strip()
for c in (0, len(lista)):
    if lista[c] == 5:
        tem5 = True
        break
lista.sort(reverse = True)
print(f"Você digitou {len(lista)} elementos.")
print(f"Os valores em ordem decrescente são: {lista}")
if tem5 == True:
    print("O cinco faz parte da lista!")
else:
    print("O cinco não faz parte da lista!")
    