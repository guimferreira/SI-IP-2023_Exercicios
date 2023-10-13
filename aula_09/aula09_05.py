from random import randint

vetora = []
vetorb = []
vetorn = []

for i in range(0, 10):
    a = randint(0, 10)
    vetora.append(a)
    b = randint(0, 10)
    vetorb.append(b)

for j in range(0, 10):
    n = vetora[j] + vetorb[j]
    vetorn.append(n)

print(vetora)
print(vetorb)
print(vetorn)
