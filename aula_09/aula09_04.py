from random import randint

vetora = []
vetorm = []

i: int

for i in range(1, 11):
    i = randint(0, 10)
    vetora.append(i)

x = int(input('Digite um nº: '))

for i in vetora:
    j = i * x
    vetorm.append(j)

print(vetora)
print(vetorm)
