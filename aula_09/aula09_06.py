from random import randint

vetor = []

while len(vetor) != 20:
    i = randint(1, 100)
    vetor.append(i)

print(vetor)

n = int(input('Nº: '))
if n in vetor:
    vetor.remove(n)

print(vetor)
