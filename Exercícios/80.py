l = []

for c in range(0, 5):
    n = int(input("Digite um valor: "))

    if c == 0:
        l.append(n)
        print("Valor adicionado ao final da lista.")
    elif n > l[-1]:
        l.append(n)
        print("Valor adicionado ao final da lista.")
    else:
        p = 0
        while p < len(l):
            if n <= l[p]:
                l.insert(p, n)
                print(f"Valor adicionado na posição {p} da lista.")
                break
            p = p + 1

print(f"Os valores adicionados em ordem foram: {l}")