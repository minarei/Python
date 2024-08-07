n = int(input("Digite um número para ver sua tabuada: "))
c = 0

for t in range(1, 11):
    c = c + 1
    print("{} x {} = {}" .format(n, c, n * c))