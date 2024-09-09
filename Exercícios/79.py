l = []

while True:
    n = int(input("Digite um valor: "))

    if n not in l:
        l.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")

    q = str(input("Quer continuar? [S/N]: "))

    if q in 'Nn':
            break

print(f"Você digitou os valores: {l}")