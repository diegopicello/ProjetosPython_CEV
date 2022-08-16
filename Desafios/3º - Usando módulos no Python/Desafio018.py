import math
an = int(input('Digite um ângulo: '))
convert = math.radians(an)
print('O ângulo de {} tem SENO de {:.3f},'.format(an, math.sin(math.radians(an)), end = ' '))
print('COSSENO DE {:.3f} e TANGENTE de {:.3f}'.format(math.cos(math.radians(an)), math.tan(math.radians(an))))





