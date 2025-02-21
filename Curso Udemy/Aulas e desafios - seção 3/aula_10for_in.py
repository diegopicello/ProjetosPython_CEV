texto = 'Ribeirão Preto'
novotexto = ''
#sei que é iterável: o for só precisa de um iterável e ele vai iterar;
for letra in texto:
    print(letra)
    novotexto += f'*{letra}'
print(novotexto + '*')
#e for com range? range -> range(start, stop, step)
#são independentes, mas funcionam bem juntos;
#a função range cria um intervalo;
numeros = range(10)#passa um número apenas, ele vai do 0 ao 10 com passo 1;
#o último valor não é incluído!
#No while, precisa do índice, no for, pega o valor especificamente;
for numero in numeros:
    print(numero)


#e como funciona o for por baixo dos panos?
texto2 = 'FEA-RP USP'
iterador = iter(texto2)
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
#o else funciona da mesma maneira no for;
#os vários níveis de for dentro de for também!
