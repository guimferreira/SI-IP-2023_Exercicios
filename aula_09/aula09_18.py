from random import randint

lista1 = list()
lista2 = list()
lista12 = list()

n_lista1 = randint(1, 5)
n_lista2 = randint(1, 5)

for n1 in range(n_lista1):
    n = randint(1, 10)
    lista1.append(n)

for n2 in range(n_lista2):
    n = randint(1, 10)
    lista2.append(n)

for i in range(1, 11):
    if i in lista1 and i in lista2:
        lista12.append(i)

print(lista1)
print(lista2)
print(lista12)
