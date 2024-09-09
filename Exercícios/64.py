c = 0
s = 0
n = 0

while n != 999:
    n = int(input("Digite um número [999 para parar]: "))
    s = s + n
    c = c + 1
    if n == 999:
        s = s - n

print(f"Você digitou {c} números e a soma entre eles é {s}.")