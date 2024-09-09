from random import randint

c = 0

while True:
    v = int(input("Diga um valor: "))
    pi = str(input("Par ou Ímpar [P/I]: ")).strip()[0]
    r = randint(0, 10)
    s = v + r

    print(f"Você jogou {v} e o computador jogou {r}. O total foi de {s} e", end = '')

    if pi in 'Pp':
        if s % 2 == 0:
            c = c + 1
            print(" você venceu porque deu par!")
        else:
            print(" o computador venceu porque deu ímpar!")
            print(f"Você venceu {c} vezes.")
            break
    if pi in 'Ii':
        if s % 2 == 1:
            c = c + 1
            print(" você venceu porque deu par!")
        else:
            print(" o computador venceu porque deu ímpar!")
            print(f"Você venceu {c} vezes.")
            break 

    print("Vamos jogar novamente...")