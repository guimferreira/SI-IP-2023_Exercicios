from random import randint

vetor = []

while len(vetor) != 20:
    n = randint(0, 100)
    if n not in vetor:
        vetor.append(n)

print(vetor)
print(f'Maior nº: {max(vetor)} | Posição: {vetor.index(max(vetor))}')
print(f'Menor nº: {min(vetor)} | Posição: {vetor.index(min(vetor))}')
