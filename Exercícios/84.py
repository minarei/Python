lista = []
dados = []
maior = 0
menor = 0

while True:
    nome = str(input("Nome: ")).strip()
    dados.append(nome)
    peso = float(input("Peso: "))
    dados.append(peso)
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados.copy())
    dados.clear()
    continuar = str(input("Quer continuar? [S/N]: "))

    if continuar in 'Nn':
        break

print(f"Ao todo, você cadastrou {len(lista)} pessoas.")
print(f"O maior peso foi de {maior}kg: ", end = '')

for p in lista:
    if p[1] == maior:
        print(f"{p[0]}")

print(f"O menor peso foi de {menor}kg: ", end = '')

for p in lista:
    if p[1] == menor:
        print(f"{p[0]}")