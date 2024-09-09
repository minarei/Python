while True:
    n = int(input("Quer ver a tabuada de qual número? "))
    c = 0
    if n < 0:
        break
    for c in range(0, 10):
        c = c + 1
        print(f"{n} x {c} = {n * c}")

print("Programa de tabuada encerrado! Volte sempre.")