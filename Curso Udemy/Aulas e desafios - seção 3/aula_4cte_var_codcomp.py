#python não diferencia var de constante: fazemos isso usando maiúscula nas cte's;
#muito if = muita complexidade de código, às vezes alguém precisa até debugar para entender;
#muito bloco dentro de bloco (afastamento da margem) = complexidade = ruim;

velocidade = float(input('Digite a velocidade atual: ')) #minha velocidade
kilometro_atual = int(input('Digite o kilômetro atual: ')) #meu lugar

RADAR_1 = 60 #radar
KILOMETRO_RADAR_1 = 100 #local do radar
RADAR_RANGE = 1 #onde o radar pega: um antes e um depois

LIMITE_INFERIOR = KILOMETRO_RADAR_1 - RADAR_RANGE
LIMITE_SUPERIOR = KILOMETRO_RADAR_1 + RADAR_RANGE

velocidade_carro_excedeu = velocidade > RADAR_1
dentro_do_range = LIMITE_INFERIOR <= kilometro_atual <= LIMITE_SUPERIOR
multa = dentro_do_range and velocidade_carro_excedeu

if multa:
    print('Você excedeu os limites de velocidade e foi multado.')
else:
    print('Dessa vez passa.')
