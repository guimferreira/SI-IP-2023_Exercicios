from random import randint

vetor = list()

while True:
    if len(vetor) == 20:
        break

    n = randint(0, 100)
    if n >= 0 and n not in vetor:
        vetor.append(n)

print(vetor)
print(f'Valor máximo: {max(vetor)}')
print(f'Valor mínimo: {min(vetor)}')
