c = 0
maior = 0
menor = 0

for pe in range(1, 6):
    c = c + 1
    p = float(input(f"Peso da {c}ª pessoa: "))
    if pe == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(f"O menor peso lido foi de {menor} quilos.")
print(f"O maior peso lido foi de {maior} quilos.")