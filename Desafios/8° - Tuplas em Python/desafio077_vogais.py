palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
'praticar', 'trabalhar', 'mercado', 'programador', 'futuro',)
for palavra in palavras:
    print(f'\nNa palavra "{palavra.upper()}" existem as vogais: ', end = '')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra} ', end = '')
