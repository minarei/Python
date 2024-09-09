v = float(input("Qual valor você quer sacar? R$"))
t = v
c = 50
tc = 0

while True:
    if t >= c:
        t = t - c
        tc = tc + 1
    else:
        print(f"Total de {tc} células de R${c} reais.")
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if t == 0:
            break