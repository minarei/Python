c = 0
maior = 0
menor = 0

for a in range(1, 7 + 1):
    c = c + 1
    ano = int(input(f"Em que ano a {c}ª pessoa nasceu? "))
    idade = 2024 - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print(f"Ao todo, nós temos {maior} pessoas maiores de idade e {menor} pessoas menores de idade.")