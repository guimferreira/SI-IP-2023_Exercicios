from random import randint

turma = []
soma = 0

nota: int

for nota in range(1, 21):
    nota = randint(0, 10)
    turma.append(nota)
    soma += nota

media = soma / 20
acima_da_media = len([nota for nota in turma if nota >= media])

print(turma)
print(f'A média da turma foi {media:.2f}.')
print(f'{acima_da_media} alunos tiveram nota acima da media da turma.')
