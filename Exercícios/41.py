ano = int(input("Ano de nascimento: "))
idade = 2024 - ano

if idade <= 9:
    print("O atleta tem {} anos, portanto sua classificação é mirim." .format(idade))
elif idade >= 10 and idade <= 14:
    print("O atleta tem {} anos, portanto sua classificação é infantil." .format(idade))
elif idade >= 15 and idade <= 19:
    print("O atleta tem {} anos, portanto sua classificação é júnior." .format(idade))
elif idade >= 20 and idade <= 25:
    print("O atleta tem {} anos, portanto sua classificação é sênior." .format(idade))
else:
    print("O atleta tem {} anos, portanto sua classificação é master." .format(idade))