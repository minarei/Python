maior18 = 0
homem = 0
mulher20 = 0

while True:
    print("Cadastre uma pessoa: ")
    idade = int(input("Idade: "))
    sexo = ' '
    continuar = ' '

    while sexo not in 'MmFf':
        sexo = str(input("Sexo [M/F]: ")).strip()[0]

    if idade > 18:
        maior18 = maior18 + 1

    if sexo in 'Mm':
            homem = homem + 1
    
    if sexo in 'Ff' and idade < 20:
            mulher20 = mulher20 + 1

    while continuar not in 'SsNn':
        continuar = str(input("Quer continuar? [S/N] ")).strip()[0]
    if continuar in 'Nn':
        break

print(f"O total de pessoas com mais de 18 anos foi {maior18}.")
print(f"Ao todo, temos {homem} homens cadastrados.")
print(f"Ao todo, temos {mulher20} mulheres com menos de 20 anos.")