c = 0
mulheres = 0
s = 0
m = 0
maioridade = 0
maiornome = ''
for pe in range(1, 5):
    c = c + 1
    print(f"{c}ª pessoa: ")
    n = str(input("Nome: ")).strip()
    i = int(input("Idade: "))
    s = str(input("Sexo: ")).strip().upper()
    s = s + i
    m = s / 4

    if pe == 1 and s == 'M':
        maioridade = i
        maiornome = n

    if s == 'M' and i > maioridade:
        maioridade = i
        maiornome = n

    if i < 20 and s == 'F':
        mulheres = mulheres + 1

print(f"A média de idade do grupo é de {m} anos.")
print(f"O homem mais velho tem {maioridade} anos e se chama {maiornome}.")
print(f"Ao todo são {mulheres} mulheres com menos de 20 anos.")