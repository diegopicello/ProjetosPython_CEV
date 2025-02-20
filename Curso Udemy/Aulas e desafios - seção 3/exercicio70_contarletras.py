frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'.lower()
i = 0
maisvezes = 0
letramaisvezes = ''
while i < len(frase):
    letraatual = frase[i]
    vezesapareceu = frase.count(letraatual)
    if vezesapareceu > maisvezes and letraatual != ' ':
        letramaisvezes = letraatual
        maisvezes = vezesapareceu
    i += 1
print(f'A letra que apareceu mais vezes foi "{letramaisvezes}" com {maisvezes} aparições na frase.')
