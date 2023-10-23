horarios = ((8,12), (14,18), (19,22))
soma = 0

for i in range(len(horarios)):
    soma += horarios[i][1] - horarios[i][0]

print(horarios)
print(soma)
