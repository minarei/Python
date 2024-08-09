print("=" * 21)
print("Progressão Aritmética")
print("=" * 21)

p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
d = p + (10 - 1) * r

for pa in range(p, d + r, r):
    print(pa)

print("Acabou!")