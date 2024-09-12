from time import sleep

def contador(início, fim, passo):
    if passo == 0:
        passo = 1

    if passo < 0:
        passo = abs(passo)

    if início > fim:
        passo = -passo
        fim -= 2

    for c in range(início, fim + 1, passo):
        print(c, end = ' ', flush = True)
        sleep(0.2)
    print()

contador(1, 10, 0)
contador(10, 0, 2)

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

contador(i, f, p)