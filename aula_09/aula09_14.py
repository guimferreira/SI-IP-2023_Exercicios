from random import randint

numeros = list()
q = int(input('QUANTOS NÚMEROS: '))
for i in range(q):
    numeros.append(randint(1, 10))

print(numeros)
print(sum(numeros))
