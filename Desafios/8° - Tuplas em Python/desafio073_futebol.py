'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Palmeiras.'''

tuplatimes = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 
'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG', 'Fortaleza', 
'Botafogo', 'Santos', 'São Paulo', 'RB Bragantino', 'Goiás', 'Coritiba',
'Ceará', 'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude',)
print(20 * '=-')
print(f'Lista de times: {tuplatimes}.')
print(20 * '=-')
print(f'Os 5 primeiros são {tuplatimes[0:5]}.')
print(20 * '=-')
print(f'Os 4 últimos colocados são {tuplatimes[-4:]}.')
print(20 * '=-')
print(f'Times em ordem alfabética: {sorted(tuplatimes)}.')
print(20 * '=-')
print(f'O palmeiras esta na {tuplatimes.index("Palmeiras") + 1}º posição.')#coloque aspas diferentes no index pois ele morre se você usa a mesma aspa do print todo!
print(20 * '=-')
