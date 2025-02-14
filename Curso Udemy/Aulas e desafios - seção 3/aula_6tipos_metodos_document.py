#built-in types: já vêm instalados.
#os imutáveis: str, int, float, bool;
#exemplo:
cidade = 'Ribeirão Preto'
#cidade[3] = 'ABC'#esse tipo de dado é imutável
#posso atribuir, mas não mudar o valor, posso apenas criar outra variável
outracidade = f'{cidade[:8:]}'
print(cidade, outracidade)
#esses 4 tipos são objetos, e objetos têm ações que podem ser feitas neles
#as ações vem na documentação no python
#exemplo:
print(cidade)
#Cada tipo tem seus próprios métodos;
