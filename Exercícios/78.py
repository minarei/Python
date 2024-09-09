l = []
ma = 0
me = 0

for p in range(0, 5):
    l.append(int(input(f"Digite um valor para a posição {p}: ")))

    if p == 0:
        ma = me = l[p]
    else:
        if l[p] > ma:
            ma = l[p]
        if l[p] < me:
            me = l[p]

print(f"Você digitou os valores: {l}")
print(f"O maior valor digitado foi {ma} nas posições: ", end = '')

for i, v in enumerate(l):
    if v == ma:
        print(f"{i}... ", end = '')
print()
print(f"O menor valor digitado foi {me} nas posições: ", end = '')

for i, v in enumerate(l):
    if v == me:
        print(f"{i}... ", end = '')
print()