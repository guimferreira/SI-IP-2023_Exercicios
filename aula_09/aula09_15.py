palavras = list()

qn = int(input('QUANTIDADE DE NOMES: '))
for i in range(qn):
    palavras.append(str(input('DIGITE O NOME: ')))

palavras_ordenadas = sorted(palavras, key=len, reverse=True)
print(palavras_ordenadas)
