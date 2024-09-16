def voto(ano):
    idade = 2024 - ano
    if idade < 18 and idade >= 16 or idade >= 70:
        return print(f"Com {idade} anos, o voto é opcional.")
    elif idade < 16:
        return print(f"Com {idade} anos, o voto é negado.")
    else:
        return print(f"Com {idade} anos, o voto é obrigatório.")
a = int(input("Em que ano você nasceu? "))
voto(a)