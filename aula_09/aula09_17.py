estoque = list()
produto = dict()
valor_estoque = 0
n = int(input('Cadastrar quantos produtos? '))

for i in range(n):
    produto['nome'] = str(input('NOME DO PRODUTO: ')).strip()
    produto['preço'] = float(input('PREÇO UNITÁRIO: R$: '))
    produto['quantidade'] = int(input('QUANTIDADE EM ESTOQUE: '))
    estoque.append(produto.copy())

for i in range(len(estoque)):
    valor_estoque += estoque[i]['preço'] * estoque[i]['quantidade']

print(estoque)
print(f'R$ {valor_estoque:.2f}')
