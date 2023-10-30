tamanho = int(input('Tamanho da lista: '))
lista_n = list()
soma = 0

while True:
    if len(lista_n) == tamanho:
        break
    n = int(input('Digite um nº: '))
    if n not in lista_n:
        lista_n.append(n)
print(lista_n)

for n in lista_n:
    if n % 2 == 0:
        soma += n

print(soma)
