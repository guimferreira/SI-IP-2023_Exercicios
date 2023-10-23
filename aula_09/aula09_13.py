lista = dict()

for i in range(5):
    nome = str(input('NOME: ')).strip().title()
    numero = int(input('NÚMERO: '))
    lista.update({nome: numero})

for k, v in lista.items():
    print(f'{k}: {v}')
