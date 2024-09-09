t = (int(input("Digite um número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o último número: ")))

print(f"Os valores digitados foram: {t}")
print(f"O valor 9 apareceu {t.count(9)} vezes.")

if 3 not in t:
    print("O valor 3 não foi digitado em nenhuma posição.")
else:
    print(f"Os valor 3 está na {t.index(3) + 1}ª posição.")

print(f"Os valores pares digitados foram: ", end = '')

for n in t:
    if n % 2 == 0:
        print(n, end = ', ')