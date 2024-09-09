c = 0
s = 0

while True:
    n = int(input("Digite um número [999 para parar]: "))
    s = s + n
    c = c + 1
    if n == 999:
        s = s - n
        break

print(f"Você digitou {c} números e a soma entre eles é {s}.")