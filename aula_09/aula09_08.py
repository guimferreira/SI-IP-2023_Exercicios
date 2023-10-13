from random import randint

vetor = []

for i in range(0, 30):
    i = randint(0, 10)
    vetor.append(i)
print(vetor)

n = int(input('Nº: '))
print(vetor.count(n))
