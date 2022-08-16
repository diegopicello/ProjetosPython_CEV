nome = str(input('Qual é o seu nome completo? ')).strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in nome))
#ou você pode fazer:
#print('Seu nome tem Silva?',end = ' ')
#print('Silva' in nome)
