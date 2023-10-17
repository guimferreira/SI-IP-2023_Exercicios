from random import randint

matriz = []
vetor = []
maior = 0

for l in range(0, 10):
    while len(vetor) < 10:
        n = randint(0, 100)
        if n not in vetor:
            vetor.append(n)
            if n > maior:
                maior = n
    matriz.append(vetor[:])
    vetor.clear()
    print(matriz[l])

print(maior)
for vetor in matriz:
    if maior in vetor:
        print(f'LINHA: {matriz.index(vetor) + 1}\nCOLUNA: {vetor.index(maior) + 1}')
