from random import randint

vetor1 = []
vetor2 = []
cont = 0

for i in range(0, 10):
    v1 = randint(0, 10)
    vetor1.append(v1)
    v2 = randint(0, 10)
    vetor2.append(v2)
    if v1 == v2:
        cont += 1

print(vetor1)
print(vetor2)
print(cont)
