matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tercoluna = []
soma = maior = menor = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))

        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        
        tercoluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
        
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end = '')
    print()

print(f"A soma dos valores pares é {soma}.")
print(f"A soma dos valores da terceira coluna é {tercoluna}.")

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f"O maior valor da segunda linha é {maior}.")