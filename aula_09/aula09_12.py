dados = dict()

dados['primeiro_nome'] = str(input('NOME: ')).strip().title()
dados['sobrenome'] = str(input('SOBRENOME: ')).strip().title()
dados['idade'] = int(input('IDADE: '))
dados['cidade'] = str(input('CIDADE: ')).strip().title()

for k, v in dados.items():
    print(f'{k}: {v}')
