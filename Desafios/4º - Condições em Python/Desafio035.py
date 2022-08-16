print('-='*20)
print('Analisador de triângulos')
print('-='*20)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Tais seguimentos podem formar um triângulo.')
else:
    print('Tais seguimentos NÃO PODEM formar um triângulo.')
