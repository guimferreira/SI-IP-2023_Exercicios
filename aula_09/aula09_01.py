times = []

while len(times) != 3:
    clube = str(input('Clube: ')).strip().title()
    if clube not in times:
        times.append(clube)
    else:
        print('Clube já está na lista. Digite outro nome.')

clube = str(input('Qual clube você torce? ')).strip().title()
if clube in times:
    print('ACHEI! Seu clube está na lista.')
else:
    print('NÃO ACHEI!')
print(times)
