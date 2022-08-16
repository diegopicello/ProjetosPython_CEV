m = float(input('Digite uma distância em metros: '))
print('a medida de {} corresponde a \n {}Km \n {}Hm \n {}Dam'.format(m, m/1000, m/100, m/10), end='\n ') 
print('{}Dm \n {} cm \n {} mm'.format(m*10, m*100, m*1000))
