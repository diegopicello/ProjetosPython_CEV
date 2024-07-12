pessoas = {'Nome':'Diego','sexo':'M','Idade':21}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos de idade.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k}={v}')
    