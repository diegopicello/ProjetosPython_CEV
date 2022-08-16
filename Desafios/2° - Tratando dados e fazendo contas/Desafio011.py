l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h
tl = a/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, h, a))
print('Para pintar essa parede, você precisará de {:.5} litros de tinta.'.format(tl))
