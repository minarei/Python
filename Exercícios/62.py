p = int(input("Primeiro número: "))
r = int(input("Razão: "))
c = 1
t = 0
total = p
m = 10

while m != 0:
    t = t + m
    while c <= t:
        print(f"{p} -> ", end = '')
        c = c + 1
        p = p + r
    print("Pausa!")
    m = int(input("Quantos termos a mais você quer mostrar? "))
print("Acabou!")
print(f"Ao todo, {t} termos foram exibidos.")