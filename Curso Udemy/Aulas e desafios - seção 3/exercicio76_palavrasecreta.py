'''"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.'''

PALAVRA_SECRETA = 'perfume'
letra_usuario = ''
palavra_formada = f'{len(PALAVRA_SECRETA)*'*'}'
tentativas = 0
while True:
    letra_usuario = input('Digite uma letra: ').strip().lower()
    if len(letra_usuario) > 1:
        print('Por favor, digite apenas uma letra.')
        continue
    tentativas += 1
    novastr = ''
    for letra in PALAVRA_SECRETA:
        if letra == letra_usuario:
            novastr += letra_usuario
        else:
            novastr += '*'
    palavrafinal = ''
    for i, caractere in enumerate(palavra_formada):
        if PALAVRA_SECRETA[i] == novastr[i] or palavra_formada[i] != '*':
            palavrafinal += PALAVRA_SECRETA[i]
        else:
            palavrafinal += '*'
    palavra_formada = palavrafinal
    print(palavra_formada)
    if palavra_formada == PALAVRA_SECRETA:
        print('Parabéns, você acertou a palavra.')
        break
print(f'Você descobriu que a palavra era {PALAVRA_SECRETA} em {tentativas} tentativas válidas.')
