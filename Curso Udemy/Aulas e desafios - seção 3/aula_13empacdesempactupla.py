"""lista é pacote de itens dentro dela: desempacotar =
criar variável com algum item;"""

nomes = ['Maria','João','Diego']

nome1, nome2, nome3 = nomes

print(nome1, nome2, nome3)

_, _, nome4, *resto = ['Maria','João','Diego'] #se deixovariável de resto sem nada para inserir nela, ela vira lista vazia
#mais valor que variável;
#resto gera outra lista com o resto da outra lista;
#convenção de programação: usar underline para indicar que não usará;
#underline no começo para pegar segundo nome
print(nome4, resto)

nomes = tuple(nomes) #posso fazer coerção
cidades = 'Ribeirão','Rio Claro' #sem parênteses gera tupla
