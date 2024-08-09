n = int(input("Digite um número: "))
s = 0

for p in range(1, n + 1):
    print(p)
    if n % p == 0:
        s = s + 1

print("O número {} foi divisível {} vezes." .format(n, s))

if s == 2:
    print("Portanto ele é um número primo.")
else:
    print("Portanto ele não é um número primo.")