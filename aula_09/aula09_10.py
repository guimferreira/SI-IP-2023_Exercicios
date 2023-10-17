from random import randint

matriz = []
vetor = []
soma = somadp = somads = somacc = 0

for l in range(0, 10):
    while len(vetor) < 10:
        n = randint(0, 100)
        if n not in vetor:
            vetor.append(n)
            soma += n
    vetor.sort()
    matriz.append(vetor[:])
    vetor.clear()
    print(matriz[l])

print(f'SOMA GERAL: {soma}')
for l in range(0, 10):
    somadp += matriz[l][l]
    somads += matriz[l][9 - l]
    somacc += matriz[l][5]
print(f'SOMA DIAGONAL PRINCIPAL: {somadp}')
print(f'SOMA DIAGONAL SECUNDÁRIA: {somads}')
print(f'SOMA COLUNA CENTRAL: {somacc}')
