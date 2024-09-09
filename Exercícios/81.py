l = []
c = 0

while True:
    v = int(input("Digite um valor: "))
    l.append(v)
    c += 1

    q = str(input("Quer continuar? [S/N]: "))

    if q in 'Nn':
        break

l.sort(reverse = True)

print(f"Você digitou {c} elementos.")
print(f"Os valores em ordem decrescente são {l}.")

print(f"O valor 5 ", end = '')

if 5 in l:
    print("foi encontrado na lista!", end = '')
else:
    print("não foi encontrado na lista!", end = '')