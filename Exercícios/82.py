l = []
lp = []
lí = []

while True:
    n = int(input("Digite um número: "))
    l.append(n)
    q = str(input("Quer continuar? [S/N]: "))

    if q in 'Nn':
        break

    if n % 2 == 0:
        lp.append(n)
    elif n % 2 == 1:
        lí.append(n)

print(f"A lista completa é {l}")
print(f"A lista de pares é {lp}")
print(f"A lista de ímpares é {lí}")