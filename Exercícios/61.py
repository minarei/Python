p = int(input("Primeiro número: "))
r = int(input("Razão: "))
c = 0

while c <= 10:
    print(f"{p} -> ", end = '')
    c = c + 1
    p = p + r

print("Acabou!")