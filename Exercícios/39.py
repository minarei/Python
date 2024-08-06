a = int(input("Ano de nascimento: "))
i = 2024 - a

print("Quem nasceu em {} vai fazer {} anos em 2024." .format(a, i))

if i < 18:
    s = 18 - i
    print("Ainda faltam {} anos para o alistamento." .format(s))
    ano = 2024 + s
    print("Seu alistamento será em {}." .format(ano))
elif i == 18:
    print("Você precisa se alistar imediatamente!")
elif i > 18:
    s = i - 18
    print("Você já deveria ter se alistado há {} anos." .format(s))
    ano = 2024 - s
    print("Seu alismento foi em {}." .format(ano))