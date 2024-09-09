n = 0
c = 0
s = 0
ma = 0
me = 0


while True:
    n = int(input("Digite um número: "))
    q = str(input("Quer continuar? [S/N] "))
    c = c + 1
    s = s + n
    m = s / c

    if c == 1:       
        ma = n
        me = n
    else:
        if n > ma:
            ma = n
        elif n < me:
            me = n


    if q in 'Ss':      
        continue
    elif q in 'Nn':
        break
    else:
        print("Valor inválido! Tente novamente.")

print(f"Você digitou {c} números e a média entre eles é {m}.")
print(f"O maior número foi {ma} e o menor foi {me}.")