texto = 'Ribeirão Preto'
novotexto = ''
#sei que é iterável: o for só precisa de um iterável e ele vai iterar;
for letra in texto:
    print(letra)
    novotexto += f'*{letra}'
print(novotexto + '*')