def leiaInt(c):
    global número
    while True:
        número = input(c).strip()
        if número.isnumeric():
            break
        else:
            print("Erro! Digite um número inteiro válido.")

n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {número}.")