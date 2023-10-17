from random import randint

matriz1 = []
matriz2 = []
matriz3 = []
matriz4 = []
matriz5 = []
matriz = [matriz1, matriz2, matriz3, matriz4, matriz5]

while True:
    i = randint(0, 100)
    if i not in matriz1 or matriz2 or matriz3 or matriz4 or matriz5:
        if len(matriz1) < 5:
            matriz1.append(i)
        elif len(matriz1) == 5 and len(matriz2) < 5:
            matriz2.append(i)
        elif len(matriz1) == 5 and len(matriz2) == 5 and len(matriz3) < 5:
            matriz3.append(i)
        elif len(matriz1) == 5 and len(matriz2) == 5 and len(matriz3) == 5 and len(matriz4) < 5:
            matriz4.append(i)
        elif len(matriz1) == 5 and len(matriz2) == 5 and len(matriz3) == 5 and len(matriz4) == 5 and len(matriz5) < 5:
            matriz5.append(i)
        # switch_case = {
        #     len(matriz1) < 5: matriz1.append(n),
        #     len(matriz1) == 5 and len(matriz2) < 5: matriz2.append(n),
        #     len(matriz1) == 5 and len(matriz2) == 5 and len(matriz3) < 5: matriz3.append(n),
        #     len(matriz1) == 5 and len(matriz2) == 5 and len(matriz3) == 5 and len(matriz4) < 5: matriz4.append(n),
        #     len(matriz1) == 5 and len(matriz2) == 5 and len(matriz3) == 5 and len(matriz4) == 5 and len(matriz5) < 5: matriz5.append(n),
        # }

    if len(matriz1) == len(matriz2) == len(matriz3) == len(matriz4) == len(matriz5) == 5:
        break

print(matriz)

x = int(input('Nº: '))
if x in matriz1 or matriz2 or matriz3 or matriz4 or matriz5:
    print('Sim')
else:
    print('Não')
